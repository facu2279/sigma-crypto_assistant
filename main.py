#!/usr/bin/python3
"""
Made by :
            - Facundo Diaz
            - Tomas De Castro
            - Tadeo Grach
for Holberton School 2021
"""
import requests
import time
url = 'https://api.binance.com/'
secret_key = 'gJX2yUILKQwEYZXrcBBLjRnV0tMcIMCpWbHgLNQab6qwMOArjqjD6dMpZlQfu2AA'
api_key = 'jDnfBQgOu3Lzc9I9WErNkicH0jp5gL3exCKwV5HvemEZDF48GRpnrOpVcFBZfZQR'


def consultar_precio_BTC(url):
    query = "api/v3/ticker/price?symbol=BTCUSDT"
    r = requests.get(url + query)
    r = r.json()
    """print(r)
    print("El precio del BTC es", r["price"])"""
    return int(float(r["price"]))

def consultar_precio_DOGE(url):
    query = "api/v3/ticker/price?symbol=DOGEUSDT"
    r = requests.get(url + query)
    r = r.json()
    """print(r)
    print("El precio del DOGE es", r["price"])"""

    return float(r["price"])

def print_precios(price_BTC, price_DOGE):
    print("El precio del BTC es ", price_BTC)
    print("El precio del DOGE es ", price_DOGE)


"""
DECLARACION DE TODAS LAS VARIABLES
"""
a = 1
price_BTC = 0
price_DOGE = 0
while(a != 0):
    price_BTC = consultar_precio_BTC(url)
    price_DOGE = consultar_precio_DOGE(url)
    print_precios(price_BTC, price_DOGE)
    a = 0

"""
DESCARTABLE
"""
def traer_todo(url):
    query = "api/v3/exchangeInfo"
    query2 = "api/v3/avgPrice?symbol=DOGEUSDT"
    query3 = "api/v3/klines?symbol=BTCUSDT&interval=1m&limit=2"
    r = requests.get(url + query3)
    r = r.json()
    for elem in r:
        print(elem)
