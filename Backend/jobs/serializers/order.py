from rest_framework import serializers
from jobs.models import Order


class OrderSerializer(serializers.ModelSerializer):
    client = serializers.ReadOnlyField(source='client.username')
    service_name = serializers.ReadOnlyField(source='service.name')

    class Meta:
        model = Order
        fields = ['id', 'client', 'service', 'service_name', 'status', 'created_at']
        read_only_fields = ['id', 'client', 'created_at']

        extra_kwargs = {
            'service': {'required': False}
        }
