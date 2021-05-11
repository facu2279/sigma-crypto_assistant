#!/usr/bin/python3
"""
Made by Facundo DiaZ - Tomas De CastrO - Tadeo Grach for Holberton School 2021 """


""" IMPORTS ARCHIVOS """
import Info
import Entidades
import Persistencia

""" IMPORTS GENERALES"""
import time
import os
from flask import Flask, render_template

"""
color fondo en hexa #262833
color logo en hexa es #39E991
"""

""" DECLARATION OF ALL VARIABLES """
a = 1
BTC = 0
DOGE = 0
ETH = 0
url = 'https://api.binance.com/'

""" FUNCTIONS """

def print_precios(price_BTC, price_DOGE, price_ETH):
    print("El precio del BTC es ", price_BTC, "USD")
    print("El precio del DOGE es ", price_DOGE, "USD")
    print("El precio del ETH es ", price_ETH, "USD")

""" HERE START PROGRAM """
while(a != 0):
    os.system('clear')
    print("WELCOME TO SIGMA\n\n")
    print("LOG IN - PRESS 0\n------\nCREATE A NEW ACCOUNT - PRESS 1")
    option = input()
    if option not in ["0", "1"]:
        print("Please, insert a valid option\n")
        time.sleep(2)
        os.system('clear')
        continue
    elif option == "0":
        """ llamar login """
        print("Insert your name")
        user = input()
        print("Insert your password")
        password = input()
        res = Persistencia.login(user, password)
        if res == 1:
            print("LOGIN PASO \n")
            a = 0
        else:
            print("NO PASO")
    else:
        """ crear user """
        b = 1
        while(b != 0):
            print("Insert your name")
            user = input()
            print("Insert your password")
            password = input()
            print("What is your favorite crypto?")
            print("Bitcoin - press 0\n")
            print("Ethereum - press 1\n")
            print("Dogecoin - press 2")
            option = input()
            if option not in ["0", "1", "2"]:
                print("Please, insert a valid option\n")
                time.sleep(2)
                os.system('clear')
                continue
            elif option == 0:
                interes = "BTC"
            elif option == 1:
                interes = "ETH"
            else:
                interes = "DOGE"
            new_user = Entidades.User(user, password, interes)
            b = 0
            os.system('clear')
            print("The user was created successfully")

    """
    BTC = Info.consultar_precio_BTC(url)
    DOGE = Info.consultar_precio_DOGE(url)
    ETH = Info.consultar_precio_ETH(url)
    print_precios(BTC, DOGE, ETH)
    a = 0"""