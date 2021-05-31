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


users = persistence.traer_users()
resumen = "aun no hay info para darte my king"
for i in range(0, len(users), 2):
    content = "Buenas tardes"
    print("enviando correo a ", users[i])
    print("que su direccion es", users[i + 1])
    nombre = str(users[i])
    correo = str(users[i + 1])
    content = content + nombre + resumen
    os.system("echo -e 'Subject: subject \n\n " + content + "' | ssmtp " + correo)