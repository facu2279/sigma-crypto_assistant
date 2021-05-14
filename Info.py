#!/usr/bin/python3
"""
Made by Facundo DiaZ - Tomas De CastrO - Tadeo Grach for Holberton School 2021 """

""" IMPORTS """
import requests


""" DECLARACION DE TODAS LAS VARIABLES """


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

def consultar_transacciones_BTC(url):
    suma = 0
    query = "api/v3/trades?symbol=BTCUSDT"
    r = requests.get(url + query)
    print(r)
    print(type(r))
    r = r.json()
    print(r, "\n\n\n")
    for i in r:
        if (i["isBuyerMaker"] == "true"):
            suma = suma + int(float((i["quoteQty"])))
        else:
            suma = suma - int(float((i["quoteQty"])))
    print("el resultado de sumar todas las transacciones compra/venta es = ", suma)
    if (suma > 0):
        print("va a subir")
    else:
        print("va a bajar")
    """for elem in r:
        print(elem)
    print(type(elem))"""
