from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from jobs.models import Review, Order, Service, Category, User


class ReviewTest(APITestCase):
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
            service=self.service,
            status='completed'
        )

    def test_client_review_success(self):
        self.client.force_authenticate(user=self.client_user)

        response = self.client.post(
            reverse('review-list'),
            {
                'order': self.order.id,
                'rating': 4,
                'comment': 'Good quality'
            },
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_worker_review_forbidden(self):
        self.client.force_authenticate(user=self.worker)

        response = self.client.post(
            reverse('review-list'),
            {
                'order': self.order.id,
                'rating': 3,
                'comment': 'I like it'
            },
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
