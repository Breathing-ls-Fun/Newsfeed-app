"""
import pytest
from django.contrib import auth, messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from newsfeed.reporter.reporter import Reporter

from user.views import (
    login, registration, query, logout, preferences
)


@pytest.fixture
def authenticated_user():
    # Create a user and authenticate
    user = auth.models.User.objects.create_user(username='testuser', password='testpass')
    user.save()
    auth.login(request, user)
    yield user
    auth.logout(request)


def test_login_authenticated_user(authenticated_user):
    # Perform the test for a logged-in user
    request = RequestFactory().post('/user/login', {'username': 'testuser', 'password': 'testpass'})
    response = login(request)
    assert isinstance(response, HttpResponseRedirect)
    assert response.url == 'home'


def test_login_invalid_credentials():
    # Perform the test for invalid credentials
    request = RequestFactory().post('/user/login', {'username': 'testuser', 'password': 'wrongpass'})
    response = login(request)
    assert isinstance(response, HttpResponseRedirect)
    assert response.url == 'login'


def test_registration_new_user():
    # Perform the test for registering a new user
    request = RequestFactory().post('/user/registration', {
        'first_name': 'John',
        'last_name': 'Doe',
        'email': 'john.doe@example.com',
        'password': 'password123',
        'confirm_password': 'password123',
        'username': 'johndoe'
    })
    response = registration(request)
    assert isinstance(response, HttpResponseRedirect)
    assert response.url == '/user/login'


def test_registration_existing_user():
    # Perform the test for registering an existing user
    request = RequestFactory().post('/user/registration', {
        'first_name': 'John',
        'last_name': 'Doe',
        'email': 'john.doe@example.com',
        'password': 'password123',
        'confirm_password': 'password123',
        'username': 'testuser'  # An existing username
    })
    response = registration(request)
    assert isinstance(response, HttpResponseRedirect)
    assert response.url == 'registration'


def test_query():
    # Perform the test for the query function
    request = RequestFactory().get('/user/query', {'query': 'news'})
    response = query(request)
    assert isinstance(response, render)


def test_logout():
    # Perform the test for the logout function
    request = RequestFactory().get('/user/logout')
    response = logout(request)
    assert isinstance(response, HttpResponseRedirect)
    assert response.url == '/'


def test_preferences_authenticated_user(authenticated_user):
    # Perform the test for the preferences function with an authenticated user
    request = RequestFactory().post('/user/preferences', {
        'location': 'New York',
        'category1': 'Sports',
        'category2': 'Tech',
        'category3': 'Art'
    })
    response = preferences(request)
    assert isinstance(response, HttpResponseRedirect)
    assert response.url == 'home'


def test_preferences_unauthenticated_user():
    # Perform the test for the preferences function with an unauthenticated user
    request = RequestFactory().post('/user/preferences', {
        'location': 'New York',
        'category1': 'Sports',
        'category2': 'Tech',
        'category3': 'Art'
    })
    response = preferences(request)
    assert isinstance(response, HttpResponseRedirect)
    assert response.url == 'login'


"""