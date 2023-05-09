import os
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth.models import User, auth


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            # return redirect('/user/personal_home')
            return redirect('home')
        else:
            messages.info(request, "Invalid username or password")
            return redirect('login')
    else:
        return render(request, 'user/login.html')


def registration(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        username = request.POST['username']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exists')
                return redirect('registration')
            else:
                user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, password=password,username=username)
                user.set_password(password)
                user.save()
                print("Account created!")
                return redirect('/user/login')
        
        else:
            messages.info(request, 'Passwords do not match')
            return redirect('registration')
    else:
        return render(request, "user/registration.html")

def query(request):
    return render(request,'query.html', {'title':'Search'})

def logout(request):
    auth.logout(request)
    return redirect('/')

def preferences(request):
    return render(request, "user/preferences.html")