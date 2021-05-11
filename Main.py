#!/usr/bin/python3
"""
Made by Facundo DiaZ - Tomas De CastrO - Tadeo Grach for Holberton School 2021 """


""" IMPORTS ARCHIVOS """
import Info

""" IMPORTS GENERALES"""
from flask import Flask, render_template

""" DECLARATION OF ALL VARIABLES """
a = 1
BTC = 0
DOGE = 0
ETH = 0
url = 'https://api.binance.com/'

""" FUNCTIONS """

def print_precios(price_BTC, price_DOGE, price_ETH):
    print("El precio del BTC es ", price_BTC, "USD")
    print("El precio del DOGE es ", price_DOGE, "USD")
    print("El precio del ETH es ", price_ETH, "USD")

""" HERE START PROGRAM """
while(a != 0):
    BTC = Info.consultar_precio_BTC(url)
    DOGE = Info.consultar_precio_DOGE(url)
    ETH = Info.consultar_precio_ETH(url)
    print_precios(BTC, DOGE, ETH)
    a = 0

