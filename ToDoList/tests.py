from django.contrib.auth.models import User
from django.urls import path
from django.test import Client
import unittest


class TestBasic(unittest.TestCase):
    def setUp(self):
        self.client = Client()
        self.credentials_register = {
            'username': 'user_register',
            'password': '1234567asdfgh'
            }
        self.credentials_login = {
            'username': 'user_login',
            'password': '1sfdg2423sdafh'
            }
        self.c = User.objects.create_user(**self.credentials_login)

    def test_urls(self):
        urls = ['', '/register/', '/login/', '/tasks/', '/create_task/']
        for url in urls:
            response = self.client.get(url)
            self.assertAlmostEqual(response.status_code, 200)

    def test_register(self):
        response = self.client.post('/register/', self.credentials_register, follow=True)
        self.assertAlmostEqual(response.status_code, 200)

    def test_login(self):
        response = self.client.post('/login/', self.credentials_login, follow=True)
        self.assertAlmostEqual(response.status_code, 200)

    def test_task(self):
        response = self.client.post('/create_task/', {'title': 'testcase', 'description': 'loremipsum', 'done': 'Completed', })
        self.assertAlmostEqual(response.status_code, 200)

    def tearDown(self):
        self.c.delete()
