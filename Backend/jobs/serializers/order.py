from rest_framework import serializers
from jobs.models import Order


class OrderSerializer(serializers.ModelSerializer):
    client_username = serializers.ReadOnlyField(source='client.username')
    service_name = serializers.ReadOnlyField(source='service.name')

    class Meta:
        model = Order
        fields = [
            'id',
            'client_username',
            'service',
            'service_name',
            'status',
            'created_at'
        ]
