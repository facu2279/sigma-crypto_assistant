#!/usr/bin/python3
"""
Made by Facundo Diaz - Tomas De Castro - Tadeo Grach for Holberton School 2021 """


""" IMPORTS EXTERN MODULES """
import time
""" IMPORTS FILES """
import persistence
import entities 
import mail
import info
import percent

""" In case url 1 is not working, changing for these
url = "https://api2.binance.com/"
url = "https://api3.binance.com/"
"""
url = "https://api.binance.com/"
i = 2

while(i >= 0):
    btc_price = info.consultar_precio_BTC(url)
    persistence.save_price_bitcoin(btc_price)
    eth_price = info.consultar_precio_ETH(url)
    persistence.save_price_ethereum(eth_price)
    doge_price = info.consultar_precio_DOGE(url)
    persistence.save_price_doge(doge_price)
    """percent.chequear_movimientos()

    if i % 60 == 0:
        percent.insert_in_tendencias()
    
    if i % 1440 == 0:
        mail.daily_resume()
    """
    percent.insert_in_tendencias()
    tendencias_btc = persistence.traer_tendencias_btc()
    tendencias_eth = persistence.traer_tendencias_eth()
    tendencias_doge = persistence.traer_tendencias_doge()
    """btc_tendencia = entities.Tendencia(tendencias_btc[1], tendencias_btc[2], tendencias_btc[3], tendencias_btc[4], tendencias_btc[5], tendencias_btc[6], tendencias_btc[7])
    print(btc_tendencia.to_dict())
    print(btc_tendencia.time)"""
    res = persistence.traer_tendencias_btc()
    for info in res:
        print(info, type(info))
    print("----------")
    print(i)
    i += 1    
    time.sleep(60)
