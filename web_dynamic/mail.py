#!/usr/bin/python3
"""
Made by Facundo Diaz - Tomas De Castro - Tadeo Grach for Holberton School 2021
"""

""" IMPORTS EXTERN MODULES """
import os
import time
import percent
""" IMPORTS FILES """
import persistence

def hacer_resumen():
    resumen = "\n This is your compilation of relevant information about cryptocurrencies today.\n\n"
    """ add btc information """
    resumen += "BITCOIN INFORMATION:\n\n"
    resumen += "The current price of bitcoin at the time of this email is U$D "
    resumen += str(persistence.traer_ultimo_precio_btc()) + "\n"
    resumen += "in the last 24 hours its price has moved "
    resumen += str(percent.porcentaje_btc_24()) + "%\n"
    resumen += "and yesterday at this same time, the bitcoin cost U$D"
    resumen += str(persistence.traer_masviejo_precio_btc()) + "\n\n"
    """ add doge information"""
    resumen += "DOGE COIN INFORMATION:\n\n"
    resumen += "The current price of doge coin at the time of this email is U$D "
    resumen += str(persistence.traer_ultimo_precio_doge()) + "\n"
    resumen += "in the last 24 hours its price has moved "
    resumen += str(percent.porcentaje_doge_24()) + "%\n"
    resumen += "and yesterday at this same time, the doge coin cost U$D"
    resumen += str(persistence.traer_masviejo_precio_doge()) + "\n\n"
    """ add eth information"""
    resumen += "ETHEREUM INFORMATION:\n\n"
    resumen += "The current price of ethereum at the time of this email is U$D "
    resumen += str(persistence.traer_ultimo_precio_eth()) + "\n"
    resumen += "in the last 24 hours its price has moved "
    resumen += str(percent.porcentaje_eth_24()) + "%\n"
    resumen += "and yesterday at this same time, the doge coin cost U$D "
    resumen += str(persistence.traer_masviejo_precio_eth()) + "\n\n"
    resumen += "To see more detailed information, click here http://tadeograchstudio.tech/\n\n"
    resumen += "Yours sincerely, Sigma corporation."
    return str(resumen)

def daily_resume():
    resumen = hacer_resumen()
    users = persistence.traer_users()
    for i in range(0, len(users), 2):
        nombre = str(users[i]) + " "
        correo = str(users[i + 1])
        with open("mail.txt", 'r+') as f:
            f.truncate(0)
            f.write("From: " + correo + "\nSubject: Daily Resume\nDear " + nombre + "," + resumen + "\n")
        os.system("ssmtp " + correo + " < mail.txt")