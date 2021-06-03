#!/usr/bin/python3
"""
Made by Facundo Diaz - Tomas De Castro - Tadeo Grach for Holberton School 2021 """

""" colour background in hexa #262833 colour of logo in hexa #39E991 """

""" IMPORTS EXTERN MODULES """
import time

""" IMPORTS FILES """
import persistence
import entities 
import mail
import info
import percent

""" In case url 1 is not changing for these
url = "https://api2.binance.com/"
url = "https://api3.binance.com/"
"""
url = "https://api.binance.com/"
i = 0

while(i < 1):
    print("vuelta numero", i)
    btc = info.consultar_precio_BTC(url)
    persistence.save_price_bitcoin(btc)
    eth = info.consultar_precio_ETH(url)
    persistence.save_price_ethereum(eth)
    doge = info.consultar_precio_DOGE(url)
    persistence.save_price_doge(doge)
    if i % 60 == 0:
        ultimos = persistence.traer_ultimos_precios_doge()
        average_doge = sum(ultimos) / len(ultimos)
        min_price_doge = min(ultimos)
        max_price_doge = max(ultimos)
        persistence.insert_new_tendencia("DOGE", str(average_doge), str(min_price_doge), str(max_price_doge))

        ultimos = persistence.traer_ultimos_precios_btc()
        average_btc = sum(ultimos) / len(ultimos)
        min_price_btc = min(ultimos)
        max_price_btc = max(ultimos)
        persistence.insert_new_tendencia("BTC", str(average_btc), str(min_price_btc), str(max_price_btc))

        ultimos = persistence.traer_ultimos_precios_eth()
        average_eth = sum(ultimos) / len(ultimos)
        min_price_eth = min(ultimos)
        max_price_eth = max(ultimos)
        persistence.insert_new_tendencia("ETH", str(average_eth), str(min_price_eth), str(max_price_eth))
        
        print("Inserte una nueva tendencia doge", min_price_doge, max_price_doge, average_doge)
        print("Inserte una nueva tendencia btc", min_price_btc, max_price_btc, average_btc)
        print("Inserte una nueva tendencia eth", min_price_eth, max_price_eth, average_eth)
    

    name = "DOGE"
    suggest = "el precio del " + str(name) + " es " + str(btc)
    btc = entities.Coin(name, btc, suggest)
    res = percent.detectar_constantes_btc()
    if res != 0:
        if res > 0:
            print("llego subida constante btc")
        else:
            print("llego bajada constante btc")
    else:
        print("no hubo subidas o bajadas constantes btc")
    
    res = percent.detectar_constantes_doge()
    if res != 0:
        if res > 0:
            print("llego subida constante doge")
        else:
            print("llego bajada constante doge")
    else:
        print("no hubo subidas o bajadas constantes doge")

    res = percent.detectar_constantes_eth()
    if res != 0:
        if res > 0:
            print("llego subida constante eth")
        else:
            print("llego bajada constante eth")
    else:
        print("no hubo subidas o bajadas constantes eth")
    i = i + 1

