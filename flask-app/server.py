#!/usr/bin/env python
import os

from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)

mongo_host = os.environ.get("MONGO_HOST")
mongo_port = int(os.environ.get("MONGO_PORT"))
client = MongoClient(mongo_host, mongo_port)


@app.route('/', methods=['GET'])
def todo():
    try:
        client.admin.command('ismaster')
    except:
        return "Server not available"
    return "Hello from the MongoDB client!\n"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.environ.get("FLASK_SERVER_PORT", 9090), debug=True)
