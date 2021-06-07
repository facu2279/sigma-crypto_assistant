#!/usr/bin/python3
"""
Made by Facundo Diaz - Tomas De Castro - Tadeo Grach for Holberton School 2021 """

""" IMPORTS FILES """
import persistence
import percent



class User:
    """ Class User """
    def __init__(self, name, mail):
        """ Init function """
        self.id = None
        self.name = name
        self.mail = mail

class Tendencia:
    """ Class Tendencia"""
    def __init__(self, name, average_price, max, min, open, close, date):
        self.name = name
        average_price = float(average_price)
        self.average_price = round(average_price, 2)
        self.max = max
        self.min = min
        self.open = open
        self.close = close
        self.date = date
        format_time = "%H:%M"
        self.date = self.date.strftime(format_time)

    def to_dict(self):
        """  """

        new = {}
        new["name"] = self.name
        new["average_price"] = self.average_price
        new["max"] = self.max
        new["min"] = self.min
        new["open"] = self.open
        new["close"] = self.close
        new["date"] = self.date
        return new

class Coin:
    """ Class Coin """
    def __init__(self, name):
        """ Init function """
        self.refresh_coin(name)

    def to_dict(self):
        """ Stores all coin new values in a dictionary """

        new = {}
        new["name"] = self.name
        new["price"] = self.price
        new["porcentaje"] = self.porcentaje
        new["mayor"] = self.mayor
        new["menor"] = self.menor
        return new
    
    def refresh_coin(self, name):
        """ Refresh al coins valus to last minute values """

        if name == "BTC":
            self.name = name
            self.price = persistence.traer_ultimo_precio_btc()
            self.porcentaje = percent.porcentaje_btc_24()
            self.mayor = persistence.traer_mayor_24_btc()
            self.menor = persistence.traer_menor_24_btc()
        elif name == "DOGE":
            self.name = name
            self.price = persistence.traer_ultimo_precio_doge()
            self.porcentaje = percent.porcentaje_doge_24()
            self.mayor = persistence.traer_mayor_24_doge()
            self.menor = persistence.traer_menor_24_doge()
        elif name == "ETH":
            self.name = name
            self.price = persistence.traer_ultimo_precio_eth()
            self.porcentaje = percent.porcentaje_eth_24()
            self.mayor = persistence.traer_mayor_24_eth()
            self.menor = persistence.traer_menor_24_eth()
