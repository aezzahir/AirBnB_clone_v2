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
from flask import render_template
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


@app.route("/python/", defaults={'text': "is_cool"}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_route(text="is cool"):
    """
    Display Python is ...
    """
    return f"Python {escape(text)}".replace("_", " ")


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """
    Is a number ...
    """
    if isinstance(n, int):
        return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n=None):
    """
    - Display a HTML page only if n is an integer:
    """
    if isinstance(n, int):
        return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
