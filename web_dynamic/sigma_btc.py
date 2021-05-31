#!/usr/bin/python3
""" """

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/bitcoin', strict_slashes=False)
def bitcoin():
    """ """
    return "<h1 style='color:blue'>Hello There!</h1>"

if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0')
