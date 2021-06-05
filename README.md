# SIGMA - YOUR CRYPTOCURRENCY ASSITANT
![](hhttps://github.com/facu2279/proyecto_final/blob/main/web_dynamic/static/img/sigma_logo.png)

This is the final Foundations project of the holberton school program. The team sought to create a product that would help non-expert users to understand the world of cryptocurrencies while advising them when it is convenient to buy and when to sell by analyzing the price rises and falls.

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

All the mentioned functions were programmed using Python, the database is managed by MySQL and all the data and functions are visible from a dynamic web developed with the Flask framework.
We extract information only from the OFFICIAL API of https://www.binance.com/ on the current prices of cryptocurrencies. All the calculations and detection algorithms were 100% developed by the Sigma team.