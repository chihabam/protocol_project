from flask import Flask
from Devices import Devices
from Room import Room

app = Flask(__name__)

if __name__ =='__main__':
   app.run(host="0.0.0.0",debug=True) 

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

