from datetime import datetime
from flask import Flask, request, jsonify
from flask_cors import CORS
from util import *

app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    print("received series get")
    return get_ser_lst(app.root_path)


@app.route('/', methods=['POST'])
def check():
    req = request.data
    return req


if __name__ == '__main__':
    app.run()
