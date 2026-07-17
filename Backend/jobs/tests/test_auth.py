from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status


class AuthenticationTest(APITestCase):
    def test_register_client_success(self):
        url = reverse('register')
        data = {
            'username': 'John',
            'email': 'john@gmail.com',
            'phone_number': '+998 91 289 49 10',
            'role': 'client',
            'password': 'john123'
        }

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_register_worker_success(self):
        url = reverse('register')
        data = {
            'username': 'Bob',
            'email': 'bob@gmail.com',
            'phone_number': '+998 91 900 81 33',
            'role': 'worker',
            'password': 'bob123'
        }

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_register_admin_role_not_allowed(self):
        url = reverse('register')
        data = {
            'username': 'user1',
            'email': 'user1@gmail.com',
            'phone_number': '+998 91 182 37 11',
            'role': 'admin',
            'password': 'user123'
        }

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_register_invalid_role(self):
        url = reverse('register')
        data = {
            'username': 'user2',
            'email': 'user2@gmail.com',
            'phone_number': '+998 91 678 11 28',
            'role': 'engineer',
            'password': 'user234'
        }

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
