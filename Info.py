#!/usr/bin/python3
"""
Made by Facundo DiaZ - Tomas De CastrO - Tadeo Grach for Holberton School 2021 """

""" IMPORTS """
import requests
import time
from datetime import datetime

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
    btc = consultar_precio_BTC(url)
    now = datetime.now()
    hora_exacta = now.strftime("%H:%M:%S")
    print("Hora:", hora_exacta, "el precio es:", btc)
    query = "api/v3/trades?symbol=BTCUSDT"
    r = requests.get(url + query)
    r = r.json()
    for i in r:
        if (i["isBuyerMaker"] == "true"):
            suma = suma + int(float((i["quoteQty"])))
        else:
            suma = suma - int(float((i["quoteQty"])))
    print("el resultado de sumar todas las transacciones compra/venta es = ", suma)
    if (suma > 0):
        print("La prediccion es que va a subir")
    else:
        print("La prediccion es que va a bajar")
    print("esperamos 3 minutos")
    time.sleep(180)
    btc1 = consultar_precio_BTC(url)
    now = datetime.now()
    hora_exacta = now.strftime("%H:%M:%S")
    print("Hora:", hora_exacta, "el precio es:", btc1)
    if (btc > btc1):
        print("efectivamente bajo")
    elif (btc1 > btc):
        print("efectivamente subio")
    else:
        print("el precio se mantuvo igual")
