#!/usr/bin/python3
"""
Made by Facundo Diaz - Tomas De Castro - Tadeo Grach for Holberton School 2021
"""

""" IMPORTS EXTERN MODULES """
import sys
import os
sys.path.append('/home/ubuntu/proyecto_final')

""" IMPORTS FILES """
import persistence
import entities
"""
content = "contenido"
os.system("echo -e 'Subject: hola \n\n " + content + "' | ssmtp tdecastroguelfi56@gmail.com")
"""
users = persistence.traer_users()

for i in range(0, len(users)):
    print("nombre:", users[i])
    print("correo:", users[i + 1])
    i = i + 2