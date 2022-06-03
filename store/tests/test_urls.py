from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from store.views import *
import cart


class TestTags(TestCase):
    def test_is_in_cart(self):
        self.assertFalse(is_in_cart(None, 1))


class TestUrl(SimpleTestCase):
    def test_signup(self):
        url = reverse('logout')
        view = resolve(url).func
        self.assertEquals(view, logout)
