#!/usr/bin/python3
"""
Made by Facundo Diaz - Tomas De Castro - Tadeo Grach for Holberton School 2021 """

""" IMPORTS EXTERN MODULES """
import sys
sys.path.append('/home/ubuntu/proyecto_final')

""" IMPORTS FILES """
import persistence
import entities 

precio_btc = persistence.traer_ultimo_precio_btc()
name = "BTC"
suggest = "va a subir"
btc = entities.Coin(name, precio_btc, suggest)
btc.to_json()