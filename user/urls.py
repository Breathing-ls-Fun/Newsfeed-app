from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('registration/', views.registration, name='registration'),
    path('search/', views.query, name='query'),
]