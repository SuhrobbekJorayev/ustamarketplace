from rest_framework import serializers
from jobs.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    client_name = serializers.ReadOnlyField(source='order.client.username')
    service_name = serializers.ReadOnlyField(source='order.service.name')

    class Meta:
        model = Review
        fields = [
            'id',
            'order',
            'rating',
            'comment',
            'created_at',
            'client_name',
            'service_name'
        ]
