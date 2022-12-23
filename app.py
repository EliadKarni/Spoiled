from datetime import datetime
from flask import Flask
from util.util import *
app = Flask(__name__)


@app.route('/')
def index():
   print('Returned an example files json')
   return {"pic1": True,
           "pic2": False,
           "pic3": True}


@app.route('/series')
def series():
    print("received series get")
    return get_ser_lst()


if __name__ == '__main__':
   app.run()

