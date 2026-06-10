from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Avg, Count
from jobs.models import Service
from jobs.serializers import ServiceSerializer
from jobs.permissions import IsWorker, IsServiceOwner
from jobs.filters import ServiceFilter


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all().annotate(
        average_rating=Avg('orders__review__rating'),
        reviews_count=Count('orders__review')
    )
    serializer_class = ServiceSerializer

    pagination_class = PageNumberPagination

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ServiceFilter

    search_fields = ['name', 'description', 'category__name']

    ordering_fields = ['price', 'created_at', 'name']

    ordering = ['-created_at']

    def get_permissions(self):
        if self.action == 'create':
            return [IsWorker()]

        if self.action in ('update', 'partial_update', 'destroy'):
            return [IsServiceOwner()]

        return [AllowAny()]
