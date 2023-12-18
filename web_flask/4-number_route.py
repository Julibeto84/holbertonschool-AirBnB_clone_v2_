#!/usr/bin/python3


"""
The module creates a script that starts a Flask web application
"""


from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
# We use route() decorator to tell Flask which URL should trigger our function
def first_route():
    return'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def define_route():
    return'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def print_text(text):
    formatted_text = text.replace('_', ' ')
    return f'C {escape(formatted_text)}'


@app.route('/python/', defaults={'text': 'is_cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def print_text_py(text):
    formatted_text = text.replace('_', ' ')
    return f'Python {escape(formatted_text)}'


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    return "{} is a number".format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

