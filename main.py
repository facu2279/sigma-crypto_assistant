#!/usr/bin/python3
"""
Made by :
            - Facundo Diaz
            - Tomas De Castro
            - Tadeo Grach
for Holberton School 2021
"""
import requests

url = 'https://api.binance.com/'
secret_key = 'gJX2yUILKQwEYZXrcBBLjRnV0tMcIMCpWbHgLNQab6qwMOArjqjD6dMpZlQfu2AA'
api_key = 'jDnfBQgOu3Lzc9I9WErNkicH0jp5gL3exCKwV5HvemEZDF48GRpnrOpVcFBZfZQR'


def consultar_precio_BTC(url):
    query = "api/v3/ticker/price?symbol=BTCUSDT"
    r = requests.get(url + query)
    r = r.json()
    print(r)
    print("El precio del BTC es", r["price"])

def traer_todo(url):
    query = "api/v3/exchangeInfo"

def consultar_precio_DOGE(url):
    query = "api/v3/ticker/price?symbol=DOGEUSDT"
    r = requests.get(url + query)
    r = r.json()
    print(r)
    print("El precio del DOGE es", r["price"])

consultar_precio_BTC(url)
consultar_precio_DOGE(url)