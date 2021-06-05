# SIGMA - YOUR CRYPTOCURRENCY ASSITANT
<img src="https://github.com/facu2279/proyecto_final/blob/main/web_dynamic/static/img/sigma_logo.png"/>

## Objective

This is the final Foundations project of the holberton school program. The team sought to create a product that would help non-expert users to understand the world of cryptocurrencies while advising them when it is convenient to buy and when to sell by analyzing the price rises and falls.

## Features and functionality

Features of this sigma interpreter:
In this version all the functionalities described below are functional to 3 cryptocurrencies (Bitcoin, Ethereum, Dogecoin)

- Price update minute by minute
- Calculation of percentages of rise / fall per hour
- Calculation of percentages of rise / fall per day
- Calculation of average, maximum and minimum price per hour
- Calculation of average, maximum and minimum price per day
- Detection of constant ups and downs that trigger alerts to the email of the subscribers to recommend buying / selling
- Generates summaries of relevant info every 24 hours that is sent to the subscribers through personalized emails
- Pages with information about crypto currencies to inform users with less experience

## Technologies

All the mentioned functions were programmed using Python, the database is managed by MySQL and all the data and functions are visible from a dynamic web developed with the Flask framework.
We extract information only from the OFFICIAL API of https://www.binance.com/ on the current prices of cryptocurrencies. All the calculations and detection algorithms were 100% developed by the Sigma team.

## Environment

This project was developed and tested on Ubuntu 16.04.6 LTS LTS using python3 (version 3.6.13)
The database was created on Version 14.14 Distrib 5.7.33
The dynamic web was developed and executed on Flask 2.0.1
The server runs our website using gunicorn tools in the version( 20.1.0)

## File Descriptions

├── README.md
├── reset_database
├── sql_querys
└── web_dynamic
    ├── entities.py
    ├── info.py
    ├── mail.py
    ├── mail.txt
    ├── objects.py
    ├── percent.py
    ├── persistence.py
    ├── process.py
    ├── sigma_btc.py
    ├── static
    │   ├── img
    │   │   ├── background-img.png
    │   │   ├── btc_log.png
    │   │   ├── doge_log.png
    │   │   ├── ethereum_logo.png
    │   │   ├── facundo.jpg
    │   │   ├── github_logo.png
    │   │   ├── gmail_logo.png
    │   │   ├── just_sigma2.png
    │   │   ├── linkedin_logo.png
    │   │   ├── mer.png
    │   │   ├── sigma_card.png
    │   │   ├── sigma_cel.png
    │   │   ├── sigma_logo.png
    │   │   ├── small_logo_header.png
    │   │   ├── small_logo.png
    │   │   ├── tadeo.jpg
    │   │   └── tomas.jpg
    │   └── styles
    │       ├── bitcoin_article.css
    │       ├── bitcoin_article.css~
    │       ├── bitcoin_common.css
    │       ├── bitcoin_filters.css
    │       ├── header.css
    │       ├── index_common.css
    │       ├── index_filters.css
    │       ├── team_common.css
    │       └── team_filters.css
    ├── templates
    │   ├── #bitcoin.html#
    │   ├── bitcoin.html
    │   ├── index.html
    │   └── team.html
    └── wsgi.py