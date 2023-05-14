from django.urls import reverse
from django.test import TestCase 

class ButtonTestCase(TestCase):

    def test_search_icon(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<i class="fa fa-search" id="search"></i>')

    def test_signup_button(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<button class="signup" id="sign-up-btn">Sign Up</button>')

    def test_login_button(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<button class="login" id="log-in-btn">Log In</button>')
    
    