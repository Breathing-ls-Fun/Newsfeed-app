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

        #self.assertContains(response, '<div id="search">')
        #self.assertContains(response, '<div class="sign-up">')
        #self.assertContains(response, '<button id="sign-up-btn">')