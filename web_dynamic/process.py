#!/usr/bin/python3
"""
Made by Facundo Diaz - Tomas De Castro - Tadeo Grach for Holberton School 2021 """

""" colour background in hexa #262833 colour of logo in hexa #39E991 """

""" IMPORTS EXTERN MODULES """
import sys
sys.path.append('/home/ubuntu/proyecto_final')
import time

""" IMPORTS FILES """
import persistence
import entities 
import web_dynamic.mail as mail
import info
import percent

""" In case url 1 is not changing for these
url = "https://api2.binance.com/"
url = "https://api3.binance.com/"
"""
url = "https://api.binance.com/"
i = 0

while(i < 2):
    btc = info.consultar_precio_BTC(url)
    persistence.save_price_bitcoin(btc)
    eth = info.consultar_precio_ETH(url)
    persistence.save_price_ethereum(eth)
    doge = info.consultar_precio_DOGE(url)
    persistence.save_price_doge(doge)
    if i % 60 == 0:
        ultimos = persistence.traer_ultimos_precios_doge()
        average_doge = sum(ultimos) / len(ultimos)
        min_price_doge = min(ultimos)
        max_price_doge = max(ultimos)
        persistence.insert_new_tendencia("DOGE", str(average_doge), str(min_price_doge), str(max_price_doge))
    name = "DOGE"
    suggest = "el precio del " + str(name) + " es " + str(doge)
    doge = entities.Coin(name, doge, suggest)
    max_doge_24 = persistence.traer_mayor_24_doge()
    min_doge_24 = persistence.traer_menor_24_doge()
    print(max_doge_24, min_doge_24)

    i = i + 1

