from django.urls import reverse
from django.test import TestCase 

class ButtonTestCase(TestCase):
    def test_signup_button(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<button type="submit">Sign Up</button>')
    
    