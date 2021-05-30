#!/usr/bin/python3
""" Made by Facundo Diaz, Tomas De Castro and Tadeo Grach to Holberton School 2021 """

import MySQLdb

MY_H = "localhost"
MY_U = "root"
MY_P = "betty"
MY_D = "sigma"


""" btc """
def save_price_bitcoin(price):
    nuevaconexion = MySQLdb.connect(host=MY_H, user=MY_U, passwd=MY_P, db=MY_D)
    consulta = nuevaconexion.cursor()
    consulta.execute("SELECT count(*) from history_btc;")
    resultado = consulta.fetchall()
    for i in resultado:
        for i2 in i:
            cant_items = i2
    if cant_items < 288:
        insertar_btc(str(price))
    else:
        borrar_ultimo_btc(str(price))

def insertar_btc(price):
    nueva = MySQLdb.connect(host=MY_H, user=MY_U, passwd=MY_P, db=MY_D)
    consulta = nueva.cursor()
    consulta.execute("INSERT INTO history_btc (name, price) VALUES ('BTC', " + str(price) + ");")
    nueva.commit()

def borrar_ultimo_btc(price):
    newxd = MySQLdb.connect(host=MY_H, user=MY_U, passwd=MY_P, db=MY_D)
    consulta = newxd.cursor()
    consulta.execute("select id from history_btc ORDER BY id ASC limit 1;")
    resultado = consulta.fetchall()
    for i in resultado:
        for i2 in i:
            id = i2
            id = str(id)
            borrar_item(id, str(price))
            
def borrar_item(id, price):
    nuevaxd = MySQLdb.connect(host=MY_H, user=MY_U, passwd=MY_P, db=MY_D)
    consulta = nuevaxd.cursor()
    consulta.execute("DELETE FROM history_btc WHERE id ="+ id)
    nuevaxd.commit()
    insertar_btc(str(price))
    
""" doge """

def save_price_doge(price):
        nuevaconexion = MySQLdb.connect(host=MY_H, user=MY_U, passwd=MY_P, db=MY_D)
        consulta = nuevaconexion.cursor()
        consulta.execute("SELECT count(*) from history_doge;")
        resultado = consulta.fetchall()
        for i in resultado:
            for i2 in i:
                cant_items = i2
        if cant_items < 288:
            insertar_doge(str(price))
        else:
            borrar_ultimo_doge(str(price))

def insertar_doge(price):
    nueva = MySQLdb.connect(host=MY_H, user=MY_U, passwd=MY_P, db=MY_D)
    consulta = nueva.cursor()
    consulta.execute("INSERT INTO history_doge (name, price) VALUES ('DOGE', " + str(price) + ");")
    nueva.commit()

def borrar_ultimo_doge(price):
    newxd = MySQLdb.connect(host=MY_H, user=MY_U, passwd=MY_P, db=MY_D)
    consulta = newxd.cursor()
    consulta.execute("select id from history_doge ORDER BY id ASC limit 1;")
    resultado = consulta.fetchall()
    for i in resultado:
        for i2 in i:
            id = i2
            id = str(id)
            borrar_item(id, str(price))

def borrar_item(id, price):
    nuevaxd = MySQLdb.connect(host=MY_H, user=MY_U, passwd=MY_P, db=MY_D)
    consulta = nuevaxd.cursor()
    consulta.execute("DELETE FROM history_doge WHERE id ="+ id)
    nuevaxd.commit()
    insertar_doge(str(price))

""" ethereum """

def save_price_ethereum(price):
    nuevaconexion = MySQLdb.connect(host=MY_H, user=MY_U, passwd=MY_P, db=MY_D)
    consulta = nuevaconexion.cursor()
    consulta.execute("SELECT count(*) from history_eth;")
    resultado = consulta.fetchall()
    for i in resultado:
        for i2 in i:
            cant_items = i2
    if cant_items < 288:
        insertar_eth(str(price))
    else:
        borrar_ultimo_eth(str(price))

def insertar_eth(price):
    nueva = MySQLdb.connect(host=MY_H, user=MY_U, passwd=MY_P, db=MY_D)
    consulta = nueva.cursor()
    consulta.execute("INSERT INTO history_eth (name, price) VALUES ('ETH', " + str(price) + ");")
    nueva.commit()

def borrar_ultimo_eth(price):
    newxd = MySQLdb.connect(host=MY_H, user=MY_U, passwd=MY_P, db=MY_D)
    consulta = newxd.cursor()
    consulta.execute("select id from history_eth ORDER BY id ASC limit 1;")
    resultado = consulta.fetchall()
    for i in resultado:
        for i2 in i:
            id = i2
            id = str(id)
            borrar_item(id, str(price))

def borrar_item(id, price):
    nuevaxd = MySQLdb.connect(host=MY_H, user=MY_U, passwd=MY_P, db=MY_D)
    consulta = nuevaxd.cursor()
    consulta.execute("DELETE FROM history_eth WHERE id ="+ id)
    nuevaxd.commit()
    insertar_eth(str(price))
