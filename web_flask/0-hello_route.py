#!/usr/bin/python3
""" Start flask app """
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Shows Hello HBNB """
    return 'Hello HBNB!'

if __name__ == "__main__":
    """ My Main Function """
    app.run(host='0.0.0.0', port=5000)
