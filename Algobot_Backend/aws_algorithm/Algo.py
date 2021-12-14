import alpaca_trade_api as tradeapi
import numpy as np
import time
import config
import json
import requests
from datetime import datetime
import mysql.connector
import os


api = tradeapi.REST(config.APCA_API_KEY_ID, config.APCA_API_SECRET_KEY,
                            base_url=config.APCA_API_BASE_URL,api_version='v2')



def get_data():
    # Returns a an numpy array of the closing prices of the past 5 minutes
    market_data = api.get_barset(symb, 'minute', limit=5)
    
    close_list = []
    for bar in market_data[symb]:
        close_list.append(bar.c)
    
    close_list = np.array(close_list, dtype=np.float64)

    return close_list

def buy(q, s): # Returns nothing, makes call to buy stock
    api.submit_order(
        symbol=s,
        qty=q,
        side='buy',
        type='market',
        time_in_force='gtc'
    )
def sell(q, s): # Returns nothing, makes call to sell stock
    api.submit_order(
        symbol=s,
        qty=q,
        side='sell',
        type='market',
        time_in_force='gtc'
    )
# Add you sql database keys here
mydb = mysql.connector.connect(
  host="",
  user="",
  password="",
  database=""
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM stocks")

symb = mycursor.fetchone()[0] # Ticker of stock you want to trade
pos_held = False


while True:
    print("Current Stock in Algobot:" + symb)
    print("Checking Price")
    
    close_list = get_data()

    ma = np.mean(close_list)
    last_price = close_list[4]

    print("Moving Average: " + str(ma))
    print("Last Price: " + str(last_price))

    # Make buy/sell decision
    # This algorithm buys or sells when the moving average crosses the most recent closing price 

    if ma + 10.0 < last_price and not pos_held: # Buy when moving average is ten cents below the last price
        print("Buy")
        buy(1, symb)
        pos_held = True
    
    elif ma - 10.0 > last_price and pos_held: # Sell when moving average is ten cents above the last price
        print("Sell")
        sell(1, symb)
        pos_held = False
    
    time.sleep(60)
