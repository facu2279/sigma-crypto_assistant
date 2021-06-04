#!/usr/bin/python3
"""
Made by Facundo Diaz - Tomas De Castro - Tadeo Grach for Holberton School 2021
"""

""" IMPORTS EXTERN MODULES """
import os
import time
import smtplib
""" IMPORTS FILES """
import persistence

def enviar_correos(resumen):
    users = persistence.traer_users()
    for i in range(0, len(users), 2):
        content = "Buenas tardes "
        nombre = str(users[i]) + " "
        correo = str(users[i + 1])
        content = content + nombre + resumen
        os.system("ssmtp " + correo + " < mail.txt")

def daily_resume():
    users = persistence.traer_users()
    for i in range(0, len(users), 2):
        content = "Buenas tardes "
        nombre = str(users[i]) + " "
        correo = str(users[i + 1])
        os.system("ssmtp " + correo + " < mail.txt")