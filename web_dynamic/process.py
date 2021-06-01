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

""" In case url 1 is not changing for these
url = "https://api2.binance.com/"
url = "https://api3.binance.com/"
"""
url = "https://api.binance.com/"
i = 0

while(i < 100):
    btc = info.consultar_precio_BTC(url)
    persistence.save_price_bitcoin(btc)
    eth = info.consultar_precio_ETH(url)
    persistence.save_price_ethereum(eth)
    doge = info.consultar_precio_DOGE(url)
    persistence.save_price_doge(doge)
    print("Actualice precios", btc, doge, eth)
    precio_btc = persistence.traer_ultimo_precio_btc()
    name = "BTC"
    suggest = "el precio del " + str(name) + " es " + str(btc)
    btc = entities.Coin(name, precio_btc, suggest)
    print("creo el object para la pagina web")
    print("llamo a enviar correos")
    resume = "El precio del BTC es " +  str(btc.price) + " El precio del DOGE es" + str(doge) + " El precio del ETHEREUM es " + str(eth)
    i = i + 1
    time.sleep(5)
    if i == 3:
        mail.enviar_correos(resume)
        break