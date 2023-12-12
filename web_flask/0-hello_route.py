#!/usr/bin/python3

"""This module uses strict_slashes=False in the path definition."""

from flask import Flask

app = Flask(__name__)

@app.route("/", strict_slashes=False) #the route() decorator to tell Flask what URL should trigger our function
def hello_world():
    return("Hello HBNB!")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
