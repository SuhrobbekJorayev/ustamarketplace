from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from jobs.models import WorkerProfile, User


class WorkerProfileTest(APITestCase):
    def setUp(self):
        self.worker = User.objects.create_user(
            username='Bob',
            password='bob123',
            role='worker'
        )

    def test_worker_edit_own_worker_profile(self):
        self.client.force_authenticate(user=self.worker)

        response = self.client.patch(
            reverse('worker-profile', args=[self.worker.id]),
            {
                'experience_years': 6
            },
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
