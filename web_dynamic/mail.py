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
        os.system("echo -e 'Subject: subject \n\n " + content + "' | ssmtp " + correo)

def daily_resume():
    remitente = "Desde gnucita <sigma.cryptocurrency.assistant@gmail.com>" 
    destinatario = "Mama de Gnucita <ddiiaazzfacu@gmail.com>" 
    asunto = "E-mal HTML enviado desde Python" 
    mensaje = """Hola!<br/> <br/> 
    Este es un <b>e-mail</b> enviando desde <b>Python</b> 
    """

    email = """From: %s 
    To: %s 
    MIME-Version: 1.0 
    Content-type: text/html 
    Subject: %s 

    %s
    """ % (remitente, destinatario, asunto, mensaje) 
    try: 
        smtp = smtplib.SMTP('localhost') 
        smtp.sendmail(remitente, destinatario, email) 
        print("Correo enviado") 
    except: 
        print("ERROR")