from rest_framework import viewsets
from jobs.models import Category
from jobs.serializers import CategorySerializer
from rest_framework.permissions import IsAdminUser, AllowAny


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('name')
    serializer_class = CategorySerializer

    def get_permissions(self):
        if self.action in ('create', 'update', 'partial_update', 'destroy'):
            return [IsAdminUser()]

        return [AllowAny()]
