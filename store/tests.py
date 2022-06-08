from django.test import TestCase
from .templatetags import custom_filter as a


# Create your tests here.
class TestTemplateTags(TestCase):
    def test_currency_concatinate(self):
        self.assertEquals(a.currency(1), "₹ 1")

    def test_currency_concatinate_positives(self):
        self.assertEquals(a.currency(100), "₹ " + '100')
        self.assertEquals(a.currency(200), "₹ " + '200')

    def test_currency_concatinate_negatives(self):
        self.assertEquals(a.currency(-100), "₹ " + '100')
        self.assertEquals(a.currency(-200), "₹ " + '200')
        self.assertNotEquals(a.currency(-300), "₹ " + '-300')

    def test_currency_concatinate_zeros(self):
        self.assertEquals(a.currency(0), "₹ " + '0')


