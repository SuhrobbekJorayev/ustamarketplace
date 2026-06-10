from rest_framework import serializers
from jobs.models import Service


class ServiceSerializer(serializers.ModelSerializer):
    average_rating = serializers.FloatField()
    reviews_count = serializers.IntegerField()

    class Meta:
        model = Service
        fields = '__all__'
