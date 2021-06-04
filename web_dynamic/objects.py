#!/usr/bin/python3
"""
Made by Facundo Diaz - Tomas De Castro - Tadeo Grach for Holberton School 2021 """


""" IMPORTS FILES """
import persistence
import entities 
import percent
import time

""" 
estructura objetos

(name, price, porcenaje_24, mayor, menor)

"""
name = ""
name2 = ""
name3 = ""
price = ""
price2 = ""
price3 = ""
porcentaje = ""
porcentaje2 = ""
porcentaje3 = ""
mayor = ""
menor = ""
mayor2 = ""
menor2 = ""
mayor3 = ""
menor3 = ""

def refresh_objects_values():
    """ BTC """
    global name, price, porcentaje, mayor, menor
    global name2, price2, porcentaje2, mayor2, menor2
    global name3, price3, porcentaje3, mayor3, menor3
    name = "BTC"
    price = persistence.traer_ultimo_precio_btc()
    porcentaje = percent.porcentaje_btc_24()
    mayor = persistence.traer_mayor_24_btc()
    menor = persistence.traer_mayor_24_btc()

    """ DOGE """
    name2 = "DOGE"
    price2 = persistence.traer_ultimo_precio_doge()
    porcentaje2 = percent.porcentaje_doge_24()
    mayor2 = persistence.traer_mayor_24_doge()
    menor2 = persistence.traer_mayor_24_doge()

    """ ETH """
    name3 = "ETH"
    price3 = persistence.traer_ultimo_precio_eth()
    porcentaje3 = percent.porcentaje_eth_24()
    mayor3 = persistence.traer_mayor_24_eth()
    menor3 = persistence.traer_mayor_24_eth()

refresh_objects_values()
btc = entities.Coin(name, price, porcentaje, mayor, menor)
doge = entities.Coin(name2, price2, porcentaje2, mayor2, menor2)
eth = entities.Coin(name3, price3, porcentaje3, mayor3, menor3)
