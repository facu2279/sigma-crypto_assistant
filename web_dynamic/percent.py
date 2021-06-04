#!/usr/bin/python3
"""
Made by Facundo Diaz - Tomas De Castro - Tadeo Grach for Holberton School 2021
"""

""" IMPORTS EXTERN MODULES """

import os
import time

""" IMPORTS FILES """
import persistence

""" CALCULA CAMBIO EN 24hs  BTC"""
def porcentaje_btc_24():
    viejo = 1
    nuevo = 1
    viejo = persistence.traer_masviejo_precio_btc()
    nuevo = persistence.traer_ultimo_precio_btc()
    viejo = int(viejo)
    nuevo = int(nuevo)
    return 100 * (nuevo - viejo) / viejo

""" CALCULA CAMBIO EN 24hs DOGE"""
def porcentaje_doge_24():
    viejo = 1
    nuevo = 1
    viejo = persistence.traer_masviejo_precio_doge()
    nuevo = persistence.traer_ultimo_precio_doge()
    viejo = int(viejo)
    nuevo = int(nuevo)
    return 100 * (nuevo - viejo) / viejo

""" CALCULA CAMBIO EN 24hs ETH"""
def porcentaje_eth_24():
    viejo = 1
    nuevo = 1
    viejo = persistence.traer_masviejo_precio_eth()
    nuevo = persistence.traer_ultimo_precio_eth()
    viejo = int(viejo)
    nuevo = int(nuevo)
    return 100 * (nuevo - viejo) / viejo

""" recive two numbers and return the percent """
def calcular_porcentaje(viejo, nuevo):
    viejo = viejo
    nuevo = nuevo
    return 100 * (nuevo - viejo) / viejo

""" detectar constantes btc cada una hora """
def detectar_constantes_btc():
    ultimos_precios = persistence.traer_ultimos_precios_btc()
    prev = int(ultimos_precios[0])
    porcentaje = 0
    counter = 0
    for i in range(1,60):
        if prev < int(ultimos_precios[i]):
            counter = counter + 1
        elif prev > int(ultimos_precios[i]):
            counter = counter - 1
        prev = int(ultimos_precios[i])
    porcentaje = calcular_porcentaje(int(ultimos_precios[0]), int(ultimos_precios[i]))
    porcentaje = str(porcentaje)
    porcentaje = porcentaje[0:6]
    porcentaje = float(porcentaje)
    if counter > 10 and porcentaje > 1:
        return porcentaje
    elif counter < -10 and porcentaje < -1:
        return porcentaje
    else:
        return 0

""" detectar constantes doge cada una hora """
def detectar_constantes_doge():
    ultimos_precios = persistence.traer_ultimos_precios_doge()
    prev = float(ultimos_precios[0])
    porcentaje = 0
    counter = 0
    for i in range(1,60):
        if prev < float(ultimos_precios[i]):
            counter = counter + 1
        elif prev > float(ultimos_precios[i]):
            counter = counter - 1
        prev = float(ultimos_precios[i])

    porcentaje = calcular_porcentaje(float(ultimos_precios[0]), float(ultimos_precios[i]))
    porcentaje = str(porcentaje)
    porcentaje = porcentaje[0:6]
    porcentaje = float(porcentaje)
    if counter > 10 and porcentaje > 1:
        return porcentaje
    elif counter < -10 and porcentaje < -1:
        return porcentaje
    else:
        return 0

""" detectar constantes eth cada una hora """
def detectar_constantes_eth():
    ultimos_precios = persistence.traer_ultimos_precios_eth()
    prev = int(ultimos_precios[0])
    porcentaje = 0
    counter = 0
    for i in range(1,60):
        if prev < int(ultimos_precios[i]):
            counter = counter + 1
        elif prev > int(ultimos_precios[i]):
            counter = counter - 1
        prev = int(ultimos_precios[i])
    porcentaje = calcular_porcentaje(int(ultimos_precios[0]), int(ultimos_precios[i]))
    porcentaje = str(porcentaje)
    porcentaje = porcentaje[0:6]
    porcentaje = float(porcentaje)
    if counter > 10 and porcentaje > 1:
        return porcentaje
    elif counter < -10 and porcentaje < -1:
        return porcentaje
    else:
        return 0

def chequear_movimientos():
    res = detectar_constantes_btc()
    if res != 0:
        if res > 0:
            """ llamar a mail """
        else:
           """ llamar a mail """   
    res = detectar_constantes_doge()
    if res != 0:
        if res > 0:
            """ llamar a mail """
        else:
            """ llamar a mail """
    res = detectar_constantes_eth()
    if res != 0:
        if res > 0:
            """ llamar a mail """
        else:
            """ llamar a mail """

def chequear_tendencias():
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
    