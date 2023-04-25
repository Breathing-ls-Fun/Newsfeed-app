from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages

def home(request):
    if not request.user.is_authenticated:
        return render(request, 'home.html', {})

    return redirect('/user/dashboard')
    



