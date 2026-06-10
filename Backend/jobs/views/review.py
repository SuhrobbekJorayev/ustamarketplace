from rest_framework import viewsets
from jobs.models import Review
from jobs.serializers import ReviewSerializer
from jobs.permissions import IsClient, IsReviewOwner
from rest_framework.permissions import AllowAny
from rest_framework.exceptions import ValidationError


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_queryset(self):
        queryset = Review.objects.all()
        service_id = self.request.query_params.get('service')

        if service_id:
            queryset = queryset.filter(order__service_id=service_id)

        return queryset

    def get_permissions(self):
        if self.action == 'create':
            return [IsClient()]

        if self.action in ('update', 'partial_update', 'destroy'):
            return [IsReviewOwner()]

        return [AllowAny()]

    def perform_create(self, serializer):
        print(serializer.errors)
        order = serializer.validated_data['order']

        if hasattr(order, 'review'):
            raise ValidationError(
                'This order already has a review'
            )

        serializer.save()
