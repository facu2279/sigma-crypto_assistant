#!/usr/bin/python3
"""
Made by Facundo DiaZ - Tomas De CastrO - Tadeo Grach for Holberton School 2021 """

""" IMPORTS """
import requests
import time


""" DECLARACION DE TODAS LAS VARIABLES """

secret_key = 'gJX2yUILKQwEYZXrcBBLjRnV0tMcIMCpWbHgLNQab6qwMOArjqjD6dMpZlQfu2AA'
api_key = 'jDnfBQgOu3Lzc9I9WErNkicH0jp5gL3exCKwV5HvemEZDF48GRpnrOpVcFBZfZQR'


""" FUNCTIONS """

def consultar_precio_BTC(url):
    query = "api/v3/ticker/price?symbol=BTCUSDT"
    r = requests.get(url + query)
    r = r.json()
    return int(float(r["price"]))

def consultar_precio_DOGE(url):
    query = "api/v3/ticker/price?symbol=DOGEUSDT"
    r = requests.get(url + query)
    r = r.json()
    return float(r["price"])

def consultar_precio_ETH(url):
    query = "api/v3/ticker/price?symbol=ETHUSDT"
    r = requests.get(url + query)
    r = r.json()
    return int(float(r["price"]))
