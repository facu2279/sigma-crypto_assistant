#!/usr/bin/python3
""" Made by Facundo Diaz, Tomas De Castro and Tadeo Grach to Holberton School 2021 """

import MySQLdb

MY_H = "localhost"
MY_U = "root"
MY_P = "betty"
MY_D = "sigma"
nuevaconexion = MySQLdb.connect(host=MY_H, user=MY_U, passwd=MY_P, db=MY_D)
consulta = nuevaconexion.cursor()
consulta.execute("SELECT * FROM coins;")
resultado = consulta.fetchall()
print(len(resultado))
for fila in resultado:
            print(fila)
print(type(fila))
nuevaconexion.close()
