#!/usr/bin/python3
"""
Made by Facundo DiaZ - Tomas De CastrO - Tadeo Grach for Holberton School 2021 """

""" IMPORTS """
import requests
import Entidades

def login(user, password):
    if user == "facu" and password == "1234":
        return 1
    else:
        return 0