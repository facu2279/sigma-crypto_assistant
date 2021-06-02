#!/usr/bin/python3
""" Made by Facundo Diaz, Tomas De Castro and Tadeo Grach to Holberton School 2021 """

import MySQLdb
import time
from datetime import datetime

MY_H = "localhost"
MY_U = "root"
MY_P = "betty"
MY_D = "sigma"






""" btc functions """
def save_price_bitcoin(price):
    nuevaconexion = MySQLdb.connect(host=MY_H, user=MY_U, passwd=MY_P, db=MY_D)
    consulta = nuevaconexion.cursor()
    consulta.execute("SELECT count(*) FROM history_coin WHERE name='BTC';")
    resultado = consulta.fetchall()
    for i in resultado:
        for i2 in i:
            cant_items = i2
    if cant_items < 1440:
        insertar_btc(str(price))
    else:
        borrar_ultimo_btc(str(price))

def insertar_btc(price):
    nueva = MySQLdb.connect(host=MY_H, user=MY_U, passwd=MY_P, db=MY_D)
    consulta = nueva.cursor()
    consulta.execute("INSERT INTO history_coin (name, price) VALUES ('BTC', " + str(price) + ");")
    nueva.commit()

def borrar_ultimo_btc(price):
    newxd = MySQLdb.connect(host=MY_H, user=MY_U, passwd=MY_P, db=MY_D)
    consulta = newxd.cursor()
    consulta.execute("SELECT id FROM history_coin WHERE name='BTC' ORDER BY id ASC LIMIT 1;")
    resultado = consulta.fetchall()
    for i in resultado:
        for i2 in i:
            id = i2
            id = str(id)
            borrar_item_btc(id, str(price))

def borrar_item_btc(id, price):
    nuevaxd = MySQLdb.connect(host=MY_H, user=MY_U, passwd=MY_P, db=MY_D)
    consulta = nuevaxd.cursor()
    consulta.execute("DELETE FROM history_coin WHERE id ="+ id)
    nuevaxd.commit()
    insertar_btc(str(price))

def traer_ultimo_precio_btc():
    newxd = MySQLdb.connect(host=MY_H, user=MY_U, passwd=MY_P, db=MY_D)
    consulta = newxd.cursor()
    consulta.execute("SELECT price FROM history_coin WHERE name='BTC' ORDER BY id DESC LIMIT 1;")
    resultado = consulta.fetchall()
    for i in resultado:
        for i2 in i:
            price = i2
    return price

def traer_ultimos_precios_btc():
    newxd = MySQLdb.connect(host=MY_H, user=MY_U, passwd=MY_P, db=MY_D)
    consulta = newxd.cursor()
    consulta.execute("SELECT price FROM history_coin WHERE name='BTC' ORDER BY id DESC LIMIT 60;")
    resultado = consulta.fetchall()
    arr_precios = []
    for i in resultado:
        for i2 in i:
            arr_precios.append(i2)
    return arr_precios

def traer_masviejo_precio_btc():
    newxd = MySQLdb.connect(host=MY_H, user=MY_U, passwd=MY_P, db=MY_D)
    consulta = newxd.cursor()
    consulta.execute("SELECT price FROM history_coin WHERE name='BTC' ORDER BY id ASC LIMIT 1;")
    resultado = consulta.fetchall()
    for i in resultado:
        for i2 in i:
            price = i2
    return price









""" doge functions ---- """

def save_price_doge(price):
        nuevaconexion = MySQLdb.connect(host=MY_H, user=MY_U, passwd=MY_P, db=MY_D)
        consulta = nuevaconexion.cursor()
        consulta.execute("SELECT COUNT(*) FROM history_coin WHERE name='DOGE';")
        resultado = consulta.fetchall()
        for i in resultado:
            for i2 in i:
                cant_items = i2
        if cant_items < 1440:
            insertar_doge(str(price))
        else:
            borrar_ultimo_doge(str(price))

def insertar_doge(price):
    nueva = MySQLdb.connect(host=MY_H, user=MY_U, passwd=MY_P, db=MY_D)
    consulta = nueva.cursor()
    consulta.execute("INSERT INTO history_coin (name, price) VALUES ('DOGE', " + str(price) + ");")
    nueva.commit()

def borrar_ultimo_doge(price):
    newxd = MySQLdb.connect(host=MY_H, user=MY_U, passwd=MY_P, db=MY_D)
    consulta = newxd.cursor()
    consulta.execute("SELECT id FROM history_coin WHERE name='DOGE' ORDER BY id ASC LIMIT 1;")
    resultado = consulta.fetchall()
    for i in resultado:
        for i2 in i:
            id = i2
            id = str(id)
            borrar_item_doge(id, str(price))

def borrar_item_doge(id, price):
    nuevaxd = MySQLdb.connect(host=MY_H, user=MY_U, passwd=MY_P, db=MY_D)
    consulta = nuevaxd.cursor()
    consulta.execute("DELETE FROM history_coin WHERE id ="+ id)
    nuevaxd.commit()
    insertar_doge(str(price))

def traer_ultimo_precio_doge():
    newxd = MySQLdb.connect(host=MY_H, user=MY_U, passwd=MY_P, db=MY_D)
    consulta = newxd.cursor()
    consulta.execute("SELECT price FROM history_coin WHERE name='DOGE' ORDER BY id DESC LIMIT 1;")
    resultado = consulta.fetchall()
    for i in resultado:
        for i2 in i:
            price = i2
    return price

def traer_ultimos_precios_doge():
    newxd = MySQLdb.connect(host=MY_H, user=MY_U, passwd=MY_P, db=MY_D)
    consulta = newxd.cursor()
    consulta.execute("SELECT price FROM history_coin WHERE name='DOGE' ORDER BY id DESC LIMIT 60;")
    resultado = consulta.fetchall()
    arr_precios = []
    for i in resultado:
        for i2 in i:
            arr_precios.append(i2)
    return arr_precios
            







""" ethereum functions """

def save_price_ethereum(price):
    nuevaconexion = MySQLdb.connect(host=MY_H, user=MY_U, passwd=MY_P, db=MY_D)
    consulta = nuevaconexion.cursor()
    consulta.execute("SELECT COUNT(*) FROM history_coin WHERE name='ETH';")
    resultado = consulta.fetchall()
    for i in resultado:
        for i2 in i:
            cant_items = i2
    if cant_items < 1440:
        insertar_eth(str(price))
    else:
        borrar_ultimo_eth(str(price))

def insertar_eth(price):
    nueva = MySQLdb.connect(host=MY_H, user=MY_U, passwd=MY_P, db=MY_D)
    consulta = nueva.cursor()
    consulta.execute("INSERT INTO history_coin (name, price) VALUES ('ETH', " + str(price) + ");")
    nueva.commit()

def borrar_ultimo_eth(price):
    newxd = MySQLdb.connect(host=MY_H, user=MY_U, passwd=MY_P, db=MY_D)
    consulta = newxd.cursor()
    consulta.execute("SELECT id FROM history_coin WHERE name='ETH' ORDER BY id ASC LIMIT 1;")
    resultado = consulta.fetchall()
    for i in resultado:
        for i2 in i:
            id = i2
            id = str(id)
            borrar_item_eth(id, str(price))

def borrar_item_eth(id, price):
    nuevaxd = MySQLdb.connect(host=MY_H, user=MY_U, passwd=MY_P, db=MY_D)
    consulta = nuevaxd.cursor()
    consulta.execute("DELETE FROM history_coin WHERE id ="+ id)
    nuevaxd.commit()
    insertar_eth(str(price))

def traer_ultimo_precio_eth():
    newxd = MySQLdb.connect(host=MY_H, user=MY_U, passwd=MY_P, db=MY_D)
    consulta = newxd.cursor()
    consulta.execute("SELECT price FROM history_coin WHERE name='ETH' ORDER BY id DESC LIMIT 1;")
    resultado = consulta.fetchall()
    for i in resultado:
        for i2 in i:
            price = i2
    return price

def traer_ultimos_precios_eth():
    newxd = MySQLdb.connect(host=MY_H, user=MY_U, passwd=MY_P, db=MY_D)
    consulta = newxd.cursor()
    consulta.execute("SELECT price FROM history_coin WHERE name='ETH' ORDER BY id DESC LIMIT 60;")
    resultado = consulta.fetchall()
    arr_precios = []
    for i in resultado:
        for i2 in i:
            arr_precios.append(i2)
    return arr_precios
            

""" TENDENCIAS """

def insert_new_tendencia(name, average, min_price, max_price):
    nuevaconexion = MySQLdb.connect(host=MY_H, user=MY_U, passwd=MY_P, db=MY_D)
    consulta = nuevaconexion.cursor()
    date = datetime.now()
    print(date)
    date = int(datetime.strptime(date, '%d/%m/%Y').strftime("%s"))
    print(date)
    consulta.execute("INSERT INTO tendencias (name, average, max_price, min_price, dateprice) VALUES ('" + name  +"', '" + average +"', '" + max_price + "', '" + min_price + "', " + date + ");")
    nuevaconexion.commit()



""" USERS INSERTS """

def insert_new_user(name, mail):
    nuevaconexion = MySQLdb.connect(host=MY_H, user=MY_U, passwd=MY_P, db=MY_D)
    consulta = nuevaconexion.cursor()
    consulta.execute("INSERT INTO users_sigma (name, mail) VALUES ('" + name  +"', '" + mail +"');")
    nuevaconexion.commit()

def traer_users():
    newxd = MySQLdb.connect(host=MY_H, user=MY_U, passwd=MY_P, db=MY_D)
    consulta = newxd.cursor()
    consulta.execute("SELECT name, mail FROM users_sigma;")
    resultado = consulta.fetchall()
    arr_correos = []
    for i in resultado:
        for i2 in i:
            arr_correos.append(i2)
    return arr_correos