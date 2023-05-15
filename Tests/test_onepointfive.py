"""

#import pytest

#def test_addition():
 #   assert 2 + 2 == 4
import pytest
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from newsfeed.reporter.reporter import Reporter
from newsfeed.reporter.weatherman import Weatherman


@pytest.fixture
def authenticated_user():
    # Create a test user and authenticate them
    user = User.objects.create_user(username='testuser', password='testpassword')
    user.is_authenticated = True
    return user


def home(request):
    news_api_key = '0c53dab69d7a40d8baa66aec200e8d8d'
    weather_api_key = '33acb338cf186037e1f0801d8945e21b'

    if request.user.is_authenticated:
        weather_location = request.user.location
    else:
        weather_location = 'New York'

    reporter = Reporter(news_api_key)
    weather = Weatherman(weather_api_key, location=weather_location)

    topnews = reporter.get_top_headlines()
    current = weather.get_current_weather()
    weekly_forecast = weather.get_daily_forecast()

    # Rest of the function code


def category(request, category):
    api_key = '0c53dab69d7a40d8baa66aec200e8d8d'
    reporter = Reporter(api_key)
    topnews = reporter.get_top_headlines(category)

    # Rest of the function code


def test_home_view():
    request = {}
    response = home(request)

    assert isinstance(response, HttpResponse)
    assert response.status_code == 200
    assert 'home.html' in response.content.decode()


def test_home_view_authenticated(authenticated_user):
    request = {'user': authenticated_user}
    response = home(request)

    assert isinstance(response, HttpResponse)
    assert response.status_code == 200
    assert 'home.html' in response.content.decode()


def test_home_view_weather_location():
    request = {}
    response = home(request)

    assert isinstance(response, HttpResponse)
    assert response.status_code == 200
    assert 'home.html' in response.content.decode()


def test_category_view():
    request = {'category': 'sports'}
    response = category(request, 'sports')

    assert isinstance(response, HttpResponse)
    assert response.status_code == 200
    assert 'category.html' in response.content.decode()


def test_reporter_instance():
    api_key = '0c53dab69d7a40d8baa66aec200e8d8d'
    reporter = Reporter(api_key=api_key)

    assert isinstance(reporter, Reporter)
    assert reporter.api_key == api_key


def test_weatherman_instance():
    api_key = '33acb338cf186037e1f0801d8945e21b'
    location = 'New York'
    weather = Weatherman(api_key=api_key, location=location)

    """