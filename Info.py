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
