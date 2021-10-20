from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'algobot/index.html')


# def login(request):
#     return render(request, 'algobot/login.html')


# Login
@login_required
def success(request):
    return render(request, "registration/success.html", {})


def register(request):
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
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
