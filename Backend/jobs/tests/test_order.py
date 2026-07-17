from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from jobs.models import Order, User, Service, Category


class OrderTest(APITestCase):
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

        self.category = Category.objects.create(
            name='Painting'
        )

        self.service = Service.objects.create(
            name='Painting walls',
            category=self.category,
            worker=self.worker,
            price=40000.00
        )

        self.order = Order.objects.create(
            client=self.client_user,
            service=self.service
        )

    def test_client_place_order_success(self):
        self.client.force_authenticate(user=self.client_user)

        data = {
            'client': self.client_user.id,
            'service': self.service.id,
        }

        response = self.client.post(
            reverse('order-list'),
            data,
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Order.objects.count(), 2)

    def test_worker_place_order_forbidden(self):
        self.client.force_authenticate(user=self.worker)

        data = {
            'client': self.client_user.id,
            'service': self.service.id,
        }

        response = self.client.post(
            reverse('order-list'),
            data,
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_worker_accept_order_success(self):
        self.client.force_authenticate(user=self.worker)

        response = self.client.patch(
            reverse('order-detail', args=[self.order.id]),
            {
                'status': 'accepted'
            },
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_worker_complete_order_success(self):
        self.client.force_authenticate(user=self.worker)

        response = self.client.patch(
            reverse('order-detail', args=[self.order.id]),
            {
                'status': 'completed'
            },
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_client_accept_order_forbidden(self):
        self.client.force_authenticate(user=self.client_user)

        response = self.client.patch(
            reverse('order-detail', args=[self.order.id]),
            {
                'status': 'accepted'
            },
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_client_cancel_order_success(self):
        self.client.force_authenticate(user=self.client_user)

        response = self.client.patch(
            reverse('order-detail', args=[self.order.id]),
            {
                'status': 'canceled'
            },
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
