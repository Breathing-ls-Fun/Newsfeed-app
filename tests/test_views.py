from django.test import TestCase, Client
from django.urls import reverse

class TestViews(TestCase):
    
    def testHome(self):
        client = Client()
        response = client.get(reverse('home'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def testSignUp(self):
        client = Client()
        response = client.get(reverse('registration'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration.html')
