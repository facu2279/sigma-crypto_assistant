#!/usr/bin/python3
"""
Made by Facundo DiaZ - Tomas De CastrO - Tadeo Grach for Holberton School 2021 """

""" IMPORTS """
import requests

class User:

    def __init__(self, name, password, interes):
        self.name = name
        self.password = password
        self.interes = interes
        