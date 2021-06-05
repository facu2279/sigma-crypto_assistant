#!/usr/bin/python3
""" """

from objects import btc, doge, eth
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """"""
    return render_template('index.html')

@app.route('/team', strict_slashes=False)
def team():
    """"""
    return render_template('team.html')


@app.route('/bitcoin', strict_slashes=False)
def bitcoin():
    """ """
    btc.refresh_coin(btc.name)
    price = btc.price
    max_price = btc.mayor
    min_price = btc.menor
    percent = btc.porcentaje
    return render_template('bitcoin.html', price=price, max_price=max_price, min_price=min_price, percent=percent, eth_percent=eth.porcentaje, doge_percent=doge.porcentaje)

@app.route('/ethereum', strict_slashes=False)
def ethereum():
    """ """
    eth.refresh_coin(eth.name)
    price = eth.price
    max_price = eth.mayor
    min_price = eth.menor
    percent = eth.porcentaje
    return render_template('ethereum.html', price=price, max_price=max_price, min_price=min_price, percent=percent, btc_percent=btc.porcentaje, doge_percent=doge.porcentaje)

@app.route('/dogecoin', strict_slashes=False)
def dogecoin():
    """ """
    doge.refresh_coin(doge.name)
    price = doge.price
    max_price = doge.mayor
    min_price = doge.menor
    percent = doge.porcentaje
    return render_template('dogecoin.html', price=price, max_price=max_price, min_price=min_price, percent=percent, btc_percent=btc.porcentaje, eth_percent=eth.porcentaje)

if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port='5000')
