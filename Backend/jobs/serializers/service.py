from rest_framework import serializers
from jobs.models import Service

from rest_framework import serializers
from jobs.models import Service


class ServiceSerializer(serializers.ModelSerializer):
    average_rating = serializers.FloatField(read_only=True, default=0)
    reviews_count = serializers.IntegerField(read_only=True, default=0)
    worker = serializers.ReadOnlyField(source='worker.id')

    class Meta:
        model = Service
        fields = [
            "id",
            "name",
            "description",
            "price",
            "category",
            "worker",
            "average_rating",
            "reviews_count",
        ]

    def create(self, validated_data):
        request = self.context.get("request")

        if request and request.user.is_authenticated:
            validated_data["worker"] = request.user
        else:
            raise serializers.ValidationError("User authenticated emas")

        return super().create(validated_data)
