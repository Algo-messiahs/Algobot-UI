from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from Algobot_Backend import portfolio_manager as pm


# Home page
def index(request):
    return render(request, 'algobot/index.html')


# Post-login success page
@login_required
def dashboard(request):
    tradeSession = pm.TradeSession()
    account = tradeSession.connect_api()
    context = {'account_number': account.account_number,
               'buying_power': account.buying_power,
               'account_status': account.status,
               'equity': account.equity,
               'cash': account.cash,
               'user_name': request.user.username,
               'gain_loss': round(tradeSession.show_gain_loss(), 2)
               }
    return render(request, "registration/dashboard.html", context)


# Register page
def signup(request):
    if request.user.is_authenticated:
        return redirect('/')

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
        return redirect('/')

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
