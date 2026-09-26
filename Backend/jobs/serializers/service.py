from rest_framework import serializers
from jobs.models import Service


class ServiceSerializer(serializers.ModelSerializer):
    average_rating = serializers.FloatField(read_only=True, default=0)
    reviews_count = serializers.IntegerField(read_only=True, default=0)

    worker = serializers.ReadOnlyField(source='worker.id')
    worker_name = serializers.ReadOnlyField(source='worker.username')
    worker_phone = serializers.ReadOnlyField(source='worker.phone_number')
    worker_avatar = serializers.ReadOnlyField(source='worker.avatar')

    class Meta:
        model = Service
        fields = [
            "id",
            "name",
            "description",
            "price",
            "category",
            "worker",
            "worker_name",
            "worker_phone",
            "worker_avatar",
            "average_rating",
            "reviews_count",
        ]
