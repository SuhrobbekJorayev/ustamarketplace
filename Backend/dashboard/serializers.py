from rest_framework import serializers
from jobs.models import (
    User,
    Service,
    Order,
    Review,
    Category,
    WorkerProfile
)
from jobs.serializers import CategorySerializer, UserSerializer, ServiceSerializer, OrderSerializer


class AdminUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'phone_number',
            'role',
            'is_active',
            'is_staff',
            'created_at'
        ]


class AdminServiceSerializer(serializers.ModelSerializer):
    category_name = serializers.ReadOnlyField(source='category.name')
    worker_name = serializers.ReadOnlyField(source='worker.username')

    class Meta:
        model = Service
        fields = [
            'id',
            'name',
            'price',
            'description',
            'category',
            'category_name',
            'worker',
            'worker_name',
            'created_at'
        ]


class AdminOrderSerializer(serializers.ModelSerializer):
    client_name = serializers.ReadOnlyField(source='client.username')
    service_name = serializers.ReadOnlyField(source='service.name')

    class Meta:
        model = Order
        fields = [
            'id',
            'client',
            'client_name',
            'service',
            'service_name',
            'status',
            'created_at'
        ]


class AdminReviewSerializer(serializers.ModelSerializer):
    client_name = serializers.ReadOnlyField(source='order.client.username')
    service_name = serializers.ReadOnlyField(source='order.service.name')

    class Meta:
        model = Review
        fields = [
            'id',
            'order',
            'client_name',
            'service_name',
            'rating',
            'comment',
            'created_at'
        ]


class AdminCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            'name',
            'created_at'
        ]


class AdminWorkerProfileSerializer(serializers.ModelSerializer):
    user_name = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = WorkerProfile
        fields = [
            'id',
            'user',
            'user_name',
            'bio',
            'experience_years',
            'location',
            'created_at'
        ]
