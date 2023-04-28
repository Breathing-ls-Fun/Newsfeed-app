from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render, redirect

def home(request):
    if not request.user.is_authenticated:
        return render(request, 'home.html', {})

    return redirect('/user/dashboard')

def registration(request):
    return render(request, 'register.html', {'title':'Sign Up'})