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

    def test_font_import(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response,'<link rel="preconnect" href="https://fonts.googleapis.com">')
        self.assertContains(response,'<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>')
        self.assertContains(response,'<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700&display=swap" rel="stylesheet">')

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
        self.assertContains(response, '<li class="categories">')
        self.assertContains(response, '<a href="/category/sports">')
        self.assertContains(response, '<a href="/category/technology">')
        self.assertContains(response, '<a href="/category/entertainment">')
        self.assertContains(response, '<a href="/category/business">')
        self.assertContains(response, '<a href="/category/health">')

    def test_weather_containers(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response, '<div class="weather-container">')
        self.assertContains(response, '<div class="current-weather-box">')
        self.assertContains(response, '<div class="forecast-weather-box">')

    def test_article_containers(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response, '<div class="news-container">')
        self.assertContains(response, '<div class="news-column">')
        self.assertContains(response, '<div class="news-article">')
        self.assertContains(response, '<img class="article-image" src= "{{ image }}">')
        self.assertContains(response, '<h3 id="article-title">')
        self.assertContains(response, '<p id="article-content">')
        