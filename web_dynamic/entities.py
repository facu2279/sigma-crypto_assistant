#!/usr/bin/python3
"""
Made by Facundo Diaz - Tomas De Castro - Tadeo Grach for Holberton School 2021 """

"""OBJECTS DECLARATIONS"""

class User:
    def __init__(self, name, mail):
        self.id = None
        self.name = name
        self.mail = mail

class Coin:
    def __init__(self, name, price, suggest):
        self.name = name
        self.price = price
        self.suggest = suggest

    def to_dict(self):
        new = {}
        new["name"] = self.name
        new["price"] = self.price
        new["suggest"] = self.suggest
        return new