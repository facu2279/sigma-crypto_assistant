#!/usr/bin/python3
"""
Made by Facundo Diaz - Tomas De Castro - Tadeo Grach for Holberton School 2021
"""

""" IMPORTS EXTERN MODULES """

import sys
import os
import time
sys.path.append('/home/ubuntu/proyecto_final')

""" IMPORTS FILES """
import persistence

""" CALCULA CAMBIO EN 24hs """
viejo = persistence.traer_masviejo_precio_btc()
nuevo = persistence.traer_ultimo_precio_btc()
viejo = int(viejo)
nuevo = int(nuevo)

porcentaje = 100 * (nuevo - viejo) / viejo
print(viejo, nuevo, porcentaje)

""" """
def detectar_constantes():
    ultimos_precios = persistence.traer_ultimos_precios_btc()
    prev = int(ultimos_precios[0])
    count = 0
    for i in range(1,12):
        if prev < int(ultimos_precios[i]):
            print("+")
            count = count + 1
        elif prev > int(ultimos_precios[i]):
            print("-")
            count = count - 1
        else:
            print("=")
        prev = int(ultimos_precios[i])
        print(ultimos_precios[i])
    if count > 1:
        return(2)
    if count < -1:
        return(1)
    return 0
