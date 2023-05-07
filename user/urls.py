from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('registration/', views.registration, name='registration'),
    path('login/', views.login, name='login'),
    path('personalizedHome/', views.personalizedHome, name='personalizedHome'),
    path('preferences/', views.preferences, name='preferences'),
    path('search/', views.query, name='query'),
    path('personal/', views.personal, name='personal')
]