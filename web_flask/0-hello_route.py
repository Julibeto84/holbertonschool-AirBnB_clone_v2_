#!/usr/bin/python3
from flask import Flask

app = Flask(__name__)

@app.route("/", strict_slashes=False) #the route() decorator to tell Flask what URL should trigger our function
def hello_world():
    return("Hello HBNB!")


