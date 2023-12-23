# app.py
from flask import Flask, jsonify
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

@app.route('/hello', methods=['GET'])
def hello_world():
    now = datetime.now()
    return jsonify(message="Hello! " + now.strftime("%Y-%m-%d %H:%M:%S"))

if __name__ == '__main__':
    app.run(debug=True)
