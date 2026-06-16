from django.db import models
from django.conf import settings


class WorkerProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='worker_profile'
    )

    bio = models.TextField(blank=True)
    experience_years = models.PositiveIntegerField(default=0)

    location = models.CharField(max_length=255, default="")

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
