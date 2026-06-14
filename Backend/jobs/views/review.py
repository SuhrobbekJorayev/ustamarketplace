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
        order = serializer.validated_data['order']
        user = self.request.user

        # 1. faqat o'z orderi
        if order.client != user:
            raise ValidationError("You can review only your own orders.")

        # 2. faqat completed
        if order.status != "completed":
            raise ValidationError("You can review only completed orders.")

        # 3. 1 order = 1 review
        if Review.objects.filter(order=order).exists():
            raise ValidationError("This order already has a review.")

        serializer.save()
