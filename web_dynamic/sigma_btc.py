#!/usr/bin/python3
""" """
from process import btc
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/bitcoin', strict_slashes=False)
def bitcoin():
    """ """
    price = btc.price
    name = btc.name
    suggest = btc.suggest
    render_template('bitcoin.html', price=price, name=name, suggest=suggest)

if __name__ == "__main__":
    """ Main Function """
    app.run(host='localhost', port=5000, debug=True)
