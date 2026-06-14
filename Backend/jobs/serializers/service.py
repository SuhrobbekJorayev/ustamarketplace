from rest_framework import serializers
from jobs.models import Service


class ServiceSerializer(serializers.ModelSerializer):
    average_rating = serializers.FloatField(read_only=True, default=0)
    reviews_count = serializers.IntegerField(read_only=True, default=0)
    worker = serializers.ReadOnlyField(source='worker.id')
    worker_name = serializers.ReadOnlyField(source='worker.username')

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
            "average_rating",
            "reviews_count",
        ]

    def create(self, validated_data):
        request = self.context.get("request")
        validated_data["worker"] = request.user
        return super().create(validated_data)
