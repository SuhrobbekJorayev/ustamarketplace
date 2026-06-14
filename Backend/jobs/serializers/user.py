from rest_framework import serializers
from jobs.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'phone_number',
            'role'
        ]
        read_only_fields = ['role']
