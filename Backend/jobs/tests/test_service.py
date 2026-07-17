from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from jobs.models import User, Category, Service


class ServiceTest(APITestCase):
    def setUp(self):
        self.client_user = User.objects.create_user(
            username='John',
            password='john123',
            role='client'
        )

        self.worker = User.objects.create_user(
            username='Bob',
            password='bob123',
            role='worker'
        )

        self.category1 = Category.objects.create(
            name='Painting'
        )

    def test_worker_create_service_success(self):
        self.client.force_authenticate(user=self.worker)

        response = self.client.post(
            reverse('service-list'),
            {
                'name': 'Painting walls',
                'category': self.category1.id,
                'worker': self.worker.id,
                'price': 40000.00
            },
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Service.objects.count(), 1)
        self.assertTrue(
            Service.objects.filter(name='Painting walls').exists()
        )

    def test_client_create_service_forbidden(self):
        self.client.force_authenticate(user=self.client_user)

        response = self.client.post(
            reverse('service-list'),
            {
                'name': 'Painting walls',
                'category': self.category1.id,
                'worker': self.client_user.id,
                'price': 45000.00
            },
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_service_invalid_category(self):
        self.client.force_authenticate(user=self.worker)

        response = self.client.post(
            reverse('service-list'),
            {
                'name': 'Painting walls',
                'category': 10,
                'worker': self.worker.id,
                'price': 35000.00
            },
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
