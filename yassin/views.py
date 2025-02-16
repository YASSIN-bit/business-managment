from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegistrationForm, LoginForm


def register(request):
    form = UserRegistrationForm()
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful!")
            return redirect('login')  # Redirect to a login page or any other page
    else:
        form = UserRegistrationForm()

    return render(request, 'register.html', {'form': form})

def login_view(request):
    form = LoginForm()
    if request.method =='POST':
        form = LoginForm(request, data = request.POST)
        # form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username =username, password = password)

            if user is not None:
                auth.login(request, user)
                messages.success(request, 'you were logged in successfully')

                return redirect('')




    return render(request, 'login.html', {'form':form})

# @login_required(login_url= 'login')
def home_page(request):
    return render(request, 'home.html')
