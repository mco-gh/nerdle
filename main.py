from flask import Flask, request, send_from_directory
from google.cloud import bigquery
import json
import random

# Initialize BigQuery data.
project = "mco-general"
bq_dataset_id = "nerdle"
bq_table_id = "nerdle"
table_id = f"{project}.{bq_dataset_id}.{bq_table_id}"
bq_client = bigquery.Client()

app = Flask(__name__)

def bq_insert(rows):
    errors = bq_client.insert_rows_json(table_id, rows)  # Make an API request.
    if not errors:
        print("New rows have been added.")
    else:
        print(f"Encountered errors while inserting rows: {errors}")

@app.route('/', methods=['POST', 'GET'])
@app.route('/<name>', methods=['POST', 'GET'])
def send(name="index.html"):
    return send_from_directory('.', name)


@app.route('/log', methods=['POST', 'GET'])
def log():
    data = json.loads(request.data)
    print(data)
    bq_insert([data])
    return "ok"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, use_reloader=True,
	    debug=True, threaded=True)
