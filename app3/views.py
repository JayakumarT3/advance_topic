from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .form import RegisterForm


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', context={'form' : form})

def login2(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            uname = form.cleaned_data.get('username')
            pwd = form.cleaned_data.get('password')
            user = authenticate(username = uname, password = pwd)
            if user:
                login(request, user)
                return redirect('home2')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', context= {'form' : form})

@login_required(login_url='login')
def home2(request):
    return render(request, 'home.html')

def logout2(request):
    logout(request)
    return redirect('login')

    