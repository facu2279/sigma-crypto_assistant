#!/usr/bin/python3
"""
Made by Facundo Diaz - Tomas De Castro - Tadeo Grach for Holberton School 2021 """

""" colour background in hexa #262833 colour of logo in hexa #39E991 """

""" IMPORTS EXTERN MODULES """
import sys
# sys.path is a list of absolute path strings
sys.path.append('/home/ubuntu/proyecto_final')

import persistence
""" IMPORTS FILES """

last_price_btc = persistence.traer_ultimo_precio_btc()
last_price_doge = persistence.traer_ultimo_precio_doge()
last_price_eth = persistence.traer_ultimo_precio_eth()