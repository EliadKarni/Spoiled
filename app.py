from datetime import datetime
from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
   print('Returned an example files json')
   return {"pic1": True,
           "pic2": False,
           "pic3": True}


if __name__ == '__main__':
   app.run()

