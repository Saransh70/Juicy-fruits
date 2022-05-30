from django.test import SimpleTestCase
from django.urls import reverse, resolve
from store.views import *


class TestUrls(SimpleTestCase):

    def test_signup(self):
        url = reverse('signup')
        view = resolve(url).func
        self.assertEquals(view, signup)
        
    def test_login(self):
        url = reverse('login')
        view = resolve(url).func
        self.assertEquals(view, login)