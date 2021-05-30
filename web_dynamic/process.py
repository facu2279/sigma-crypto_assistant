#!/usr/bin/python3
"""
Made by Facundo Diaz - Tomas De Castro - Tadeo Grach for Holberton School 2021 """

""" IMPORTS EXTERN MODULES """
import sys
sys.path.append('/home/ubuntu/proyecto_final')

""" IMPORTS FILES """
import persistence


last_price_btc = persistence.traer_ultimo_precio_btc()
last_price_doge = persistence.traer_ultimo_precio_doge()
last_price_eth = persistence.traer_ultimo_precio_eth()

print("last price of btc", last_price_btc)
print("last price of doge", last_price_doge)
print("last price of eth", last_price_eth)