from datetime import datetime
from flask import Flask, request, jsonify
from flask_cors import CORS
from util import *
from Validator import return_errors

app = Flask(__name__)
CORS(app)


@app.route('/', endpoint='index', methods=['GET'])
@return_errors
def index():
    print("received series get")
    return get_ser_lst()


@app.route('/', endpoint='check', methods=['POST'])
@return_errors
def check():
    req = request.data
    return req


if __name__ == '__main__':
    app.run()
