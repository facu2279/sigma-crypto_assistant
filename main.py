#!/usr/bin/python3
"""
Made by Facundo Diaz - Tomas De Castro - Tadeo Grach for Holberton School 2021 """

""" colour background in hexa #262833 colour of logo in hexa #39E991 """

""" IMPORTS EXTERN MODULES """
import time

""" IMPORTS FILES """
import persistence
import info

""" In case url 1 is not changing for these
url = "https://api2.binance.com/"
url = "https://api3.binance.com/"
"""
url = "https://api.binance.com/"


print("empezo")
for i in range(0,300):
        btc = info.consultar_precio_BTC(url)
        persistence.save_price_bitcoin(btc)
        eth = info.consultar_precio_ETH(url)
        persistence.save_price_ethereum(eth)
        doge = info.consultar_precio_DOGE(url)
        persistence.save_price_doge(doge)
print("termino")
print("test insert new user")
persistence.insert_new_user("pedro", "holahola@hotmal.com")
print("termino inser user")