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

os.system('su Sigma')
time.sleep(2)
os.system('echo -e "sigma\n"')
"""
users = persistence.traer_users()
resumen = "  no hay info para darte my king"
for i in range(0, len(users), 2):
    content = "Buenas tardes "
    nombre = str(users[i])
    correo = str(users[i + 1])
    content = content + nombre + resumen
    os.system("echo -e 'Subject: subject \n\n " + content + "' | ssmtp " + correo)"""
os.system('ls')