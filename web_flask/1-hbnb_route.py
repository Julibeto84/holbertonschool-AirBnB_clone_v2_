#!/usr/bin/python3

"""This module uses strict_slashes=False in the path definition."""

from flask import Flask

app = Flask(__name__)

"""the route() decorator to tell Flask what URL should trigger our function"""


@app.route("/hbnb", strict_slashes=False)
def hello_world():
    return("HBNB")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
