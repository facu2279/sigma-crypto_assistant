#!/usr/bin/python3
"""
Made by Facundo Diaz - Tomas De Castro - Tadeo Grach for Holberton School 2021 """

""" IMPORTS """
import requests


"""OBJECTS DECLARATIONS"""

class User:
""" Class Users """
    def __init__(self):
        self.id_user = ""
        self.name = ""
        self.user = ""
        self.password = ""
        self.mail = ""

class Coin:
""" Class Coin """
    def __init__(self):
        self.id_coin = 0
        self.name = ""
        self.price = 0
        self.max_price

class Suggest:
""" Class Suggest """
    def __init__(self):
        self.id_suggest = 0
        self.id_coin = 0
        self.info = ""
