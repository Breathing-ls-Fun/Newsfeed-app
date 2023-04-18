# example/urls.py
from django.urls import path

from test1.views import index


urlpatterns = [
    path('test/', index),
]