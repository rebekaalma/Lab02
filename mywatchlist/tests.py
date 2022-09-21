from urllib import response
from django.test import TestCase, Client
from django.urls import resolve

# Create your tests here.
class ContohAppTest(TestCase):
    def test_contoh_app_url_exist(self):
        response = Client().get('http://localhost:8000/mywatchlist/html/')
        self.assertEqual(response.status_code,200)

class ContohAppTest(TestCase):
    def test_contoh_app_url_exist(self):
        response = Client().get('http://localhost:8000/mywatchlist/xml/')
        self.assertEqual(response.status_code,200)

class ContohAppTest(TestCase):
    def test_contoh_app_url_exist(self):
        response = Client().get('http://localhost:8000/mywatchlist/json/')
        self.assertEqual(response.status_code,200)
