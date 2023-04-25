from os import uname
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages


def login(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('psw')
        user = authenticate(request, uname = username, psw = password)
        if user is not None:
            auth_login(request, user)
            return redirect('/user/personal_home.html')
        else:
            return render(request, 'user/login.html', {'error_message': 'Invalid login'})
    else:
        return render(request, 'user/login.html')

def registration(request):
    return render(request, 'registration.html', {'title':'Sign Up'})

def query(request):
    return render(request,'query.html', {'title':'Search'})

def logout(request):
    auth_logout(request)
    return redirect('/')