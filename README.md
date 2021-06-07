# SIGMA - YOUR CRYPTOCURRENCY ASSITANT
<img src="https://github.com/facu2279/proyecto_final/blob/main/web_dynamic/static/img/sigma_logo.png"/>

## Objective

This is the final foundation project of the holberton school program. The slogan was to think of an innovative and creative idea and then create an mvp. The team sought to create a product that would help the average person understand the world of cryptocurrencies easily while advising them when to buy and when to sell by analyzing price rises and falls.

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

- This project was developed and tested on Ubuntu 16.04.6 LTS using python3 (version 3.6.13)
- The database was created on Version 14.14 Distrib 5.7.33
- The dynamic web was developed and executed on Flask 2.0.1
- The server runs our website using gunicorn tools in the version( 20.1.0)

## Copyright and licencing information
```
MIT License

Copyright (c) 2021 sigma

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## File Map
```
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
    │       ├── bitcoin_common.css
    │       ├── bitcoin_filters.css
    │       ├── header.css
    │       ├── index_common.css
    │       ├── index_filters.css
    │       ├── team_common.css
    │       └── team_filters.css
    ├── templates
    │   ├── bitcoin.html
    │   ├── index.html
    │   └── team.html
    └── wsgi.py
```

## File Descriptions

- reset_database : This file contains a script to delete the database and create it again and load enough test data for the program to run without any problem.
- sql_querys : This file contains a small script that serves to test that the number of inserts in the tables is 1440 and this means that it is working well
- entities.py : This file contains the declaration of all the classes / objects that are used
- info.py : This file contains all the requests we make to the binance api to extract the prices
- mail.py : This file contains all the functions that correspond to the use of emails and alerts
- mail.txt : This file is the one we use to generate the structure of the default emails
- objects.py : This file has the function of instantiating the objects to later be imported by the web
- percent.py : This file has all the functions that calculate percentages, detect constants and insert trends
- persistence.py : This file has all the functions that communicate with the database
- process.py : This file is the main one, it is the one that runs all the time and calls the necessary functions every x amount of time
- sigma_btc.py : This file is in charge of passing the variables and running the templates using flask
- bitcoin_article.css : This file is a css stylesheet
- bitcoin_common.css : This file is a css stylesheet
- bitcoin_filters.css : This file is a css stylesheet
- header.css : This file is a css stylesheet
- index_common.css : This file is a css stylesheet
- index_filters.css : This file is a css stylesheet
- team_common.css : This file is a css stylesheet
- team_filters.css : This file is a css stylesheet
- bitcoin.html : This file contains the html structure of the bitcoin page
- index.html : This file contains the html structure of the main page
- team.html : This file contains the html structure of the team section page
- wsgi.py : This file is necessary to run the unicorn correctly

## Known bugs

This project is still in under construction, therefore bugs may be present. If you find any, you're welcome to let us know

## Authors
Made by [Facundo Diaz](https://github.com/facu2279), [Tadeo Grach](https://github.com/tadeograch) and [Tomas de Castro](https://github.com/tomi1710) for Holberton School 2021 

## Social Networks

### Facundo Diaz

<img src="https://github.com/facu2279/proyecto_final/blob/main/web_dynamic/static/img/facundo.jpg"/>

- [Linkedin](https://www.linkedin.com/in/facundo-diaz-noya/)
- Mail: ddiiaazzfacu@gmail.com
- [Github](https://github.com/facu2279)

### Tadeo Grach

<img src="https://github.com/facu2279/proyecto_final/blob/main/web_dynamic/static/img/tadeo.jpg"/>

- [Linkedin](https://www.linkedin.com/in/tadeo-grach-toledo/)
- Mail: tade.g.17@gmail.com
- [Github](https://github.com/tadeograch)

### Tomas de Castro

<img src="https://github.com/facu2279/proyecto_final/blob/main/web_dynamic/static/img/tomas.jpg"/>

- [Linkedin](https://www.linkedin.com/in/tomas-de-castro-guelfi-1872a1211/)
- Mail: tdecastroguelfi56@gmail.com
- [Github](https://github.com/tomi1710)
