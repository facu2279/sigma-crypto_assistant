#!/usr/bin/python3

import requests

query = "https://api1.binance.com"
r = requests.get(query)
print(r)
"""
r = r.json()
symbols = r["symbols"]
"""
"""print(type(symbols))"""
"""
for elem in symbols:
    print("NUEVO ELEMENTO \n\n\n\n")
    print("new y el type de este elemento es ", type(elem), "el elem es ", elem, "\n\n")

    for key, value in elem.items():
        print(key, value, type(value))
    print("----------\n\n\n---------")
    print("new y el type de este elemento es ", type(elem2), "el elem es ", elem2, "\n\n")"""


    """print("FIN NUEVO ELEMENTO \n\n\n\n")"""
"""
for key in r_dict.keys():
    for value in r_dict.values():
        if key == "symbols" and type(value) != int:
            for i in value:
                for i2 in i.keys():
                    if i2 == "quoteAsset":
                        print(i[i2])
                        break
"""