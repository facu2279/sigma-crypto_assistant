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

viejo = persistence.traer_masviejo_precio_btc()
nuevo = persistence.traer_ultimo_precio_btc()
viejo = int(viejo)
nuevo = int(nuevo)

porcentaje = nuevo / 100 * (viejo-nuevo)
print(viejo, nuevo, porcentaje)