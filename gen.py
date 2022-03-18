import datetime
import json
import numpy
import random
from google.cloud import bigquery


# Initialize BigQuery data.
project = "mco-general"
bq_dataset_id = "nerdle"
bq_table_id = "nerdle"
table_id = f"{project}.{bq_dataset_id}.{bq_table_id}"
bq_client = bigquery.Client()

def bq_insert(rows):
    errors = bq_client.insert_rows_json(table_id, rows)  # Make an API request.
    if not errors:
        print("New rows have been added.")
    else:
        print(f"Encountered errors while inserting rows: {errors}")

guess_dist = {
    1: 1,
    2: 80,
    3: 600,
    4: 1200,
    5: 400,
    6: 200
}
total = sum(guess_dist.values())
guess_probs = { i: guess_dist[i]/total for i in guess_dist }
win_prob_at_six = .6

rows = []
row_count = 0
row_limit = 10000
current = datetime.datetime(2022, 3, 1)
per_day_count = {}

while current < datetime.datetime.now():
    for i in range(int(random.random() * 10)):
        timestamp = str(current)
        guesses = str(numpy.random.choice(list(guess_probs.keys()), p=list(guess_probs.values())))
        won = True
        if guesses == '6':
            won = random.random() <= win_prob_at_six
        data = { "timestamp": timestamp, "won": won, "guesses": guesses }
        #print(data)
        rows.append(data)
        row_count += 1
        if row_count >= row_limit:
            print(f"inserting {len(rows)} rows")
            bq_insert(rows)
            rows = []
            row_count = 0
    current += datetime.timedelta(seconds=1)
if rows:
    bq_insert(rows)
