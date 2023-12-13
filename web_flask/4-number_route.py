#!/usr/bin/python3

"""Starts a Flask web application."""

from flask import Flask
from markupsafe import escape

app = Flask(__name__)

"""the route() decorator to tell Flask what URL should trigger our function"""


@app.route("/", strict_slashes=False)
def hello_world():
    return("Hello HBNB!")


@app.route("/hbnb", strict_slashes=False)
def Hello():
    return("HBNB")


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """Displays 'C' followed by the value of <text>."""
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """Displays 'Python' followed by the value of <text>."""
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
