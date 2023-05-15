from django.test import TestCase, Client
from django.urls import reverse

class TestViews(TestCase):
    
    def test_home(self):
        client = Client()
        response = client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_sign_up(self):
        client = Client()
        response = client.get(reverse('registration'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user/registration.html')

    def test_login(self):
        client = Client()
        response = client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user/login.html')

    def test_preferences(self):
        client = Client()
        response = client.get(reverse('preferences'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user/preferences.html')

    def test_query(self):
        client = Client()
        response = client.get(reverse('query') + 'query=knicks')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user/query.html')

