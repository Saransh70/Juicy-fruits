from django.test import TestCase, Client
from django.urls import reverse


class Test_views(TestCase):
    def test_login(self):
        client = Client()
        response = client.get(reverse('login'))
        self.assertTemplateUsed(response, 'login.html')

    def test_signup(self):
        client = Client()
        response = client.get(reverse('signup'))
        self.assertTemplateUsed(response, 'signup.html')