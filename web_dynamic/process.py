#!/usr/bin/python3
"""
Made by Facundo Diaz - Tomas De Castro - Tadeo Grach for Holberton School 2021 """

""" IMPORTS EXTERN MODULES """
import sys
sys.path.append('/home/ubuntu/proyecto_final')

""" IMPORTS FILES """
import persistence


lasts_price_btc = persistence.traer_ultimos_precios_btc()
suma = 0
for i in lasts_price_btc:
    suma = suma + int(i)
print("la suma de todos los precios en la ultima hora es", suma)
print("promedio", suma/len(lasts_price_btc))
