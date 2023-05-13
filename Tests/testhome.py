from django.test import TestCase
from django.urls import reverse

class HomeTemplateTests(TestCase):
    def test_home_page_title(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response, '<title>NewsFeed</title>')

    def test_home_page_fontawesome(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response, 'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css')
        self.assertContains(response, 'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css')

    def test_home_page_navbar(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response, '<nav>')
        self.assertContains(response, '<div class="genres">')
        self.assertContains(response, '<div id="sports">')
        self.assertContains(response, '<div id="tech">')
        self.assertContains(response, '<div id="art">')
        self.assertContains(response, '<div id="politics">')
        self.assertContains(response, '<div id="food">')
        self.assertContains(response, '<div class="logo">')


    def test_newsfeed_page_today_weatherbox(self):
        response = self.client.get(reverse('newsfeed'))
        self.assertContains(response, '<div class="today-weatherbox">')
        self.assertContains(response, '<div id="weather">')
        self.assertContains(response, '<h2 id="forecast-font">Today\'s Weather</h2>')
        self.assertContains(response, '<div class="weather-icon">')
        self.assertContains(response, '<div class="today-temperature">')
        self.assertContains(response, '<p>80°F/45°F</p>')



    def test_newsfeed_page_weatherbox(self):
        response = self.client.get(reverse('newsfeed'))
        self.assertContains(response, '<div class="weather-box">')
        self.assertContains(response, '<div id="weather">')
        self.assertContains(response, '<h2 id="forecast-font">7 Day Forecast - Location: New York, NY</h2>')
        self.assertContains(response, '<div class="weather-icon">')
        self.assertContains(response, '<div class="temperature">')
        self.assertContains(response, '<p>80°F/45°F</p>')
        self.assertContains(response, '<p>75°F/50°F</p>')
        self.assertContains(response, '<p>82°F/47°F</p>')
        self.assertContains(response, '<p>70°F/42°F</p>')
        self.assertContains(response, '<p>75°F/44°F</p>')
        self.assertContains(response, '<p>79°F/43°F</p>')
        self.assertContains(response, '<p>81°F/46°F</p>')

        #self.assertContains(response, '<div id="search">')
        #self.assertContains(response, '<div class="sign-up">')
        #self.assertContains(response, '<button id="sign-up-btn">')