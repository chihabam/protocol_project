from flask import Flask
from flask_restful import Api
from Device import Device 
from Room import Room 
from Home import Home

app = Flask(__name__)

if __name__ =='__main__':
   app.run(host="0.0.0.0",debug=True) 

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

r = Home(True,True, 65)
r.leave_routine()
