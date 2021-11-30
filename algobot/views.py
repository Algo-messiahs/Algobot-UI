import json

import alpaca_trade_api as tradeapi
import datetime as dt
from datetime import date, timedelta

import simplejson as simplejson
from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from Algobot_Backend import portfolio_manager as pm, config



# Home page
def index(request):
    return render(request, 'algobot/index.html')


# Post-login success page
@login_required
def dashboard(request):
    # API call for 'portfolio_history'
    api = tradeapi.REST(config.APCA_API_KEY_ID, config.APCA_API_SECRET_KEY,
                            base_url=config.APCA_API_BASE_URL,api_version='v2')

    tradeSession = pm.TradeSession()
    account = tradeSession.connect_api()

    # Get current date
    today = date.today()
    td = timedelta(14)

    # Portfolio History
    port_hist = api.get_portfolio_history(date_start=str(today-td), date_end=None, period=None, timeframe="1D", extended_hours=None)

    # Position Symbols
    assets = tradeSession.get_all_assets()
    assetSymbols = []
    for asset in assets:
        assetSymbols.append(asset.symbol)

# all asset symbols
    all_assets = tradeSession.list_all_assets()
    all_asset_symbols = []
    for an_asset in all_assets:
        all_asset_symbols.append(an_asset.symbol)
    print("Top 10",all_asset_symbols)

    # List of timestamps formatted to YYYY-MM-DD
    tmstps = []
    for times in port_hist.timestamp:
        time = dt.datetime.fromtimestamp(times).strftime("%Y-%m-%d")
        tmstps.append(time)
    print("TMTPS:", tmstps)
    context = {'account_number': account.account_number,
               'buying_power': round(float(account.buying_power),2),
               'account_status': account.status,
               'equity': account.equity,
               'cash': account.cash,
               'user_name': request.user.username,
               'gain_loss': round(tradeSession.show_gain_loss(), 2),
               'currency': account.currency,
               'portfolio_value': account.portfolio_value,
               'long_market_value': account.long_market_value,
               'short_market_value': account.short_market_value,
                'regt_buying_power': account.regt_buying_power,
               'maintenance_margin': account.maintenance_margin,
               'initial_margin': account.initial_margin,
               'market_status' : tradeSession.market_is_open(),
               'portfolio_history': port_hist,
               'timestamps': tmstps,
               'list_of_position': assetSymbols,
               'list_of_assets': all_asset_symbols

               }
    return render(request, "registration/dashboard/dashboard.html", context)


# Register page
def signup(request):
    if request.user.is_authenticated:
        return redirect('/dashboard')

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('success')
        else:
            return render(request, 'registration/register.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'registration/register.html', {'form': form})

#Sign in page
def signin(request):
    if request.user.is_authenticated:
        return redirect('/dashboard')

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            form = AuthenticationForm()
            return render(request, 'registration/login.html', {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, 'registration/login.html', {'form': form})


def sell_stock(request):

    # Instatiate API
    api = tradeapi.REST(config.APCA_API_KEY_ID, config.APCA_API_SECRET_KEY,
                        base_url=config.APCA_API_BASE_URL, api_version='v2')
    tradeSession = pm.TradeSession()
    account = tradeSession.connect_api()

    # Get Symbol and Quantity from template
    symbol = request.POST.get("symbol")
    quantity = request.POST.get("quantity")

    # Sell stock
    response = tradeSession.sellStock(symbol=symbol, quantity=quantity)

    # Create JSON Object with API response
    api_response = {'Success': response }

    data = simplejson.dumps(api_response)

    return HttpResponse(data, content_type='application/json')

def buy_stock(request):

    # Instatiate API
    api = tradeapi.REST(config.APCA_API_KEY_ID, config.APCA_API_SECRET_KEY,
                        base_url=config.APCA_API_BASE_URL, api_version='v2')
    tradeSession = pm.TradeSession()
    account = tradeSession.connect_api()

    # Get Symbol and Quantity from template
    symbol = request.POST.get("symbol")
    quantity = request.POST.get("quantity")

    # Buy stock
    response = tradeSession.buyStock(symbol=symbol, quantity=quantity)

    # Create JSON Object with API response
    api_response = {'Success': response }

    data = simplejson.dumps(api_response)

    return HttpResponse(data, content_type='application/json')