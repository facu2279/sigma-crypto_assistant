#!/usr/bin/python3
"""
Made by Facundo Diaz - Tomas De Castro - Tadeo Grach for Holberton School 2021 """

"""
color fondo en hexa #262833
color logo en hexa es #39E991
"""


""" IMPORTS """
import persistence
import info

url = "https://api.binance.com/"
print("empezo")
for i in range(0,20):
    price = info.consultar_precio_BTC(url)
    persistence.save_price_bitcoin(price)
print("termino")
