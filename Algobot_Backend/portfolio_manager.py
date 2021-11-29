import datetime

import alpaca_trade_api as tradeapi
import os

import websocket, json

from pathlib import Path
import sys
path_root = Path(__file__).parent
sys.path.append(str(path_root))
print(path_root)
#print(sys.path)


import config


class TradeSession:

    def __init__(self):
        self.api = tradeapi.REST(config.APCA_API_KEY_ID, config.APCA_API_SECRET_KEY,
                            base_url=config.APCA_API_BASE_URL,api_version='v2')
       # Extract apca_api_key and secret key from databse per user 
       # going to look like this   
       # parser = argparse.ArgumentParser()
       # parser.add_argument('--key-id', help='APCA_API_KEY_ID')
       # parser.add_argument('--secret-key', help='APCA_API_SECRET_KEY')
       # parser.add_argument('--base-url')
       # args = parser.parse_args()
       # using mysql
                   

    # Account Connectivity Test
    def connect_api(self):
        account = self.api.get_account()
        print(account)
        return account
    # once user inters api key have them test it 
    # connect this to front end with descrption "test connect" after user inputs api key and secret key
        

    # Checking for stock testing
    def look_up_stock(self):
        userInput = input("Enter Stock Name Example Apple(AAPL): ")
        aapl = self.api.get_barset(userInput, 'day')
        print(aapl.df)
        return aapl.df
    # have this communicate to front end and let user input what they want to look up

    #ACCOUNT
    def show_buying_power(self):
        account = self.api.get_account()
        # get api account from databse

        # Check if our account is restricted from trading.
        if account.trading_blocked:
            print('Account is currently restricted from trading.')

        # Check how much money we can use to open new positions.
        print('${} is available as buying power.'.format(account.buying_power))
        return account.buying_power

    def show_gain_loss(self):
        account = self.api.get_account()
        # get key from databse 

        # Check our current balance vs. our balance at the last market close
        balance_change = float(account.equity) - float(account.last_equity)
        print(f'Today\'s portfolio balance change: ${balance_change}')
        return balance_change

    def list_all_assets(self):
        # Get a list of all active assets.
        active_assets =self. api.list_assets(status='active')

        #Filter the assets down to just those on NASDAQ.
        nasdaq_assets = [a for a in active_assets if a.exchange == 'NASDAQ']
        print(nasdaq_assets)

    def get_all_assets(self):
        # Get a list of all active assets.
        active_assets = self.api.list_positions()

        return active_assets



    def buy(self): # Returns nothing, makes call to buy stock
        self.api.submit_order(
            symbol= input("Enter Stock Name Example Apple(AAPL): "),
            qty= input("Input Qty: "),
            side='buy',
            type='market',
            time_in_force='gtc'
    )
        userInput = input # takes user input
        print("Stock ordered")
 
    def sell(self): # Returns nothing, makes call to sell stock
        self.api.submit_order(
            symbol= input("Enter Stock Name Example Apple(AAPL): "),
            qty= input("Input Qty: "),
            side='sell',
            type='market',
            time_in_force='gtc'
        )
        userInput = input # takes user input
        print("Stock sold")

    # Sell Stock given the symbol and quantity
    def sellStock(self,symbol,quantity):  # Returns nothing, makes call to sell stock
        try:
            self.api.submit_order(symbol= symbol,qty= quantity,side='sell',type='market',time_in_force='gtc')
            return 'true'
        except:
            return 'false'



        # check if stock market is open
    def market_is_open(self):

        # Check if the market is open now.
        clock = self.api.get_clock()

        if clock.is_open:
            return 'Open'
        return 'Closed'

        print('The market is {}'.format('open.' if clock.is_open else 'closed.'))
        # Check when the market was open on Dec. 1, 2018
        # date = datetime.date.today()
        # calendar = self.api.get_calendar(start=date, end=date)[0]
        # print('The market opened at {} and closed at {} on {}.'.format(
        #     calendar.open,
        #     calendar.close,
        #     date
        # ))

    def is_tradable(self,asset):
        my_asset = self.api.get_asset(asset)
        if my_asset.tradable:
            return True
        return False

    def get_market_stream(self):
        socket = "wss://data.alpaca.markets/stream"
        ws = websocket.WebSocketApp(socket, on_open=on_open, on_message=on_message, on_error=on_error,
                                    on_close=on_close)
        ws.run_forever()


    # CLI that selects user bot options
    # It is used to call from the test 
    # It is connected to the Alpaca API as well 
def cli():
    print("--------------------------------------------------------------------------")
    print("                     Welcome to AlgoBot Project                           ")
    print("--------------------------------------------------------------------------")
    print("              Please select number option you would like to do             ")
    print("                                                                          ")
    print("1. Account Information")
    print("2. Buying Power")
    print("3. List Assets")
    print("4. Show Gains and Losses")
    print("5. Look Up Stock Price")
    print("6. Buy Stock ")
    print("7. Sell Stock")
    print("8. Market Stream")
    print("9. Exit AlgoBot Project")
def menu():
    cli()
    ''' Main menu to choose an item ''' 
    chosen_element = 0
    chosen_element = input("Enter a selection from 1 to 9 : ")
    if int(chosen_element) == 1:
        print('Account Information')
        x.connect_api()
        menu()
        # Call Account information Method
    elif int(chosen_element) == 2:
        # Call Stock Price Look up methond
        print('Your buying power is: ')
        x.show_buying_power()
        menu()
    elif int(chosen_element) == 3:
        # call List of Assets Method
        print('List of Assets')
        x.list_all_assets()
        menu()
    elif int(chosen_element) == 4:
        # Call Gains and Losses 
        print('Your Gains and Losses\n')
        print("Gain/Loss: ",x.show_gain_loss())
        menu() # keeps menu tab open to make next selection and not close
    elif int(chosen_element) == 5:
        # Look up stock price 
        # this has user input so the user will have to input stock they would like to look up 
        # example Tesla = TSLA, Apple = AAPL etc
        print('Look Up Stock Price')
        x.look_up_stock()
        menu()
        # exits the menu when 6 is selected.
    elif int(chosen_element) == 6:
        print('buy')
        x.buy()
        print("Stock ordered")
        menu()      
    elif int(chosen_element) == 7:
        print('Sell')
        x.sell()
        print("Stock sold")
        menu()        
    elif int(chosen_element) == 8:
        print('Look Up Market Stream')
        x.get_market_stream()
        menu()
    elif int(chosen_element) == 9:
        print('Goodbye!')
        sys.exit() 
    else:
        print('Sorry, the value entered must be a number from 1 to 6, then try again!')


# Market Stream
def on_open(ws):
    print("opened")
    auth_data = {
        "action": "authenticate",
        "data": {"key_id": config.APCA_API_KEY_ID, "secret_key": config.APCA_API_SECRET_KEY}
    }
    ws.send(json.dumps(auth_data))
    listen_message = {"action": "listen", "data": {"streams": ["T.SPY"]}}
    ws.send(json.dumps(listen_message))

def on_error(ws, error):
    print(error)

def on_message(ws, message):
    print("received a message")
    print(message)

def on_close( ws,close_status_code, close_msg):
    print("closed connection")

if __name__ == '__main__':
    x = TradeSession()
    menu()
    cli()
    # for testing purposes
    #x.show_buying_power()
    #print("Current buying power: ",x.show_buying_power())
    #print("Gain/Loss: ",x.show_gain_loss())
    #x.list_assets()
    #x.list_all_assets(api)
    #print(x.is_tradable(api,"AAPL"))
    # testing aws pipline