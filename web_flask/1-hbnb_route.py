#!/usr/bin/python3
""" Start flask app """
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Shows Hello HBNB when / is requested """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Shows Hello HBNB when /hbtn is requested """
    return 'HBNB'

if __name__ == "__main__":
    """ My Main Function """
    app.run(host='0.0.0.0', port=5000)
