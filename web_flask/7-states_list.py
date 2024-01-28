#!/usr/bin/python3
"""Start Web App"""
from models import storage
from models.state import State
from flask import Flask, render_template

app = Flask(__name__)


@app.teardown_appcontext
def teardown_appcontext(exception):
    """
    close all session
    """
    storage.close()


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """
    displays all cities by states
    """
    states_dict = storage.all(State)
    list_states = []
    for state in states_dict.values():
        list_states.append(state)
    sorted_states = sorted(list_states, key=lambda x: x.name)
    return render_template("8-cities_by_states.html", states=sorted_states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
