from django.shortcuts import render, redirect
from django.http import HttpResponse

def home(request):
    if not request.user.is_authenticated:
        return render(request, 'home.html', {})

    return redirect('/user/dashboard')
    
def login(request):
    return render(request, 'login.html', {'title':'Login'})

def registration(request):
    return render(request, 'registration.html', {'title':'Sign Up'})

def query(request):
    return render(request,'query.html', {'title':'Search'})
