from rest_framework import serializers
from jobs.models import WorkerProfile
from jobs.serializers import UserSerializer


class WorkerProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = WorkerProfile
        fields = [
            'user',
            'bio',
            'experience_years',
            'location'
        ]
