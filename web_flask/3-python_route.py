#!/usr/bin/python3
"""
Starts a Flask web application:
    Your web application must be listening on 0.0.0.0, port 5000
    Routes:
        /: display “Hello HBNB!”
        /hbnb: display “HBNB”
    You must use the option strict_slashes=False in your route definition
"""
from flask import Flask
from markupsafe import escape
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """
    Display Hello HBNB!
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    Display HBNB
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_route(text):
    """
    Display C is ...
    """
    return f'C {escape(text).replace("_", " ")}'


@app.route("/python/<text>", strict_slashes=False)
def python_route(text):
    """
    Display Python is ...
    """
    return f'Python {escape(text).replace("_", " ")}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
