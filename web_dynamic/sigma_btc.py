#!/usr/bin/python3
""" """

import process
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/bitcoin', strict_slashes=False)
def bitcoin():
    """ """
    price = process.btc.price
    name = process.btc.name
    suggest = process.btc.suggest
    render_template('bitcoin.html', price=price, name=name, suggest=suggest)

@app.route('/team', strict_slashes=False)
def team():
    """ """
    render_template('team.html')

@app.route('/index', strict_slashes=False)
def index():
    """"""
    render_template('index.html')

if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port='5000')
