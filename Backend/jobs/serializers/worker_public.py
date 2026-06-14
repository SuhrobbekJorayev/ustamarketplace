from rest_framework import serializers
from jobs.models import User


class WorkerPublicSerializer(serializers.ModelSerializer):
    bio = serializers.ReadOnlyField(source='worker_profile.bio')
    experience_years = serializers.ReadOnlyField(source='worker_profile.experience_years')
    location = serializers.ReadOnlyField(source='worker_profile.location')

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "phone_number",
            "bio",
            "experience_years",
            "location"
        ]
