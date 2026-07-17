from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from jobs.models import Category, User


class CategoryTest(APITestCase):
    def setUp(self):
        self.admin = User.objects.create_user(
            username='admin1',
            password='admin123',
            role='admin'
        )

        self.worker = User.objects.create_user(
            username='Bob',
            password='bob123',
            role='worker'
        )

        self.category1 = Category.objects.create(name='Plumbing')
        self.category2 = Category.objects.create(name='Electrician')

    def test_create_category_as_admin(self):
        self.client.force_authenticate(user=self.admin)

        response = self.client.post(
            reverse('category-list'),
            {
                'name': 'Painting'
            },
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_category_without_authentication(self):
        response = self.client.post(
            reverse('category-list'),
            {
                'name': 'Carpenter'
            },
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_category_as_non_admin_forbidden(self):
        self.client.force_authenticate(user=self.worker)

        response = self.client.post(
            reverse('category-list'),
            {
                'name': 'Carpenter'
            },
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
