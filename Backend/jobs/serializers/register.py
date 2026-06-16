from rest_framework import serializers
from jobs.models import User, WorkerProfile


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'phone_number',
            'password',
            'role'
        )
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)

        if user.role == 'worker':
            WorkerProfile.objects.create(user=user)

        return user
