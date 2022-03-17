from flask import Flask, send_from_directory
import random

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
@app.route('/<name>', methods=['POST', 'GET'])
def send(name="index.html"):
    return send_from_directory('.', name)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, use_reloader=True,
	    debug=True, threaded=True)
