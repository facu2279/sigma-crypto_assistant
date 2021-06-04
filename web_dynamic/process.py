#!/usr/bin/python3
"""
Made by Facundo Diaz - Tomas De Castro - Tadeo Grach for Holberton School 2021 """

""" colour background in hexa #262833 colour of logo in hexa #39E991 """

""" IMPORTS EXTERN MODULES """
import time

""" IMPORTS FILES """
import persistence
import entities 
import mail
import info
from objects import btc, doge, eth
import percent

""" In case url 1 is not changing for these
url = "https://api2.binance.com/"
url = "https://api3.binance.com/"
"""
url = "https://api.binance.com/"
i = 0

while(i >= 0):
    btc_price = info.consultar_precio_BTC(url)
    persistence.save_price_bitcoin(btc_price)
    eth_price = info.consultar_precio_ETH(url)
    persistence.save_price_ethereum(eth_price)
    doge_price = info.consultar_precio_DOGE(url)
    persistence.save_price_doge(doge_price)

    if i % 60 == 0:
        percent.chequear_tendencias()
        percent.chequear_movimientos()

    print(btc)
    print(doge)
    print(eth)
    i = i + 1

