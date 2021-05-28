#!/usr/bin/python3
"""
Made by Facundo Diaz - Tomas De Castro - Tadeo Grach for Holberton School 2021 """

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
    btc = consultar_precio_BTC(url)
    now = datetime.now()
    hora_exacta = now.strftime("%H:%M:%S")
    print("Hora:", hora_exacta, "el precio es:", btc)
