#!/usr/bin/python3
""" Start flask app """
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Shows Hello HBNB """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Shows Hello HBNB when /hbtn is requested """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """ Shows a Message when /c is requested """
    return "C " + text.replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text='is_cool'):
    """ Shows a message when /python is called """
    return "Python " + text.replace('_', ' ')

if __name__ == "__main__":
    """ My Main Function """
    app.run(host='0.0.0.0', port=5000)
