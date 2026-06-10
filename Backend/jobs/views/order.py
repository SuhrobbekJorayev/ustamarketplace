from rest_framework import viewsets
from jobs.models import Order
from jobs.serializers import OrderSerializer
from jobs.permissions import IsClient, IsOrderParticipant
from rest_framework.permissions import IsAuthenticated


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        if user.role == 'worker':
            return Order.objects.filter(service__worker=user)

        return Order.objects.filter(client=user)

    def get_permissions(self):
        if self.action == 'create':
            return [IsAuthenticated(), IsClient()]

        if self.action in (
            'retrieve',
            'update',
            'partial_update',
            'destroy'
        ):
            return [IsAuthenticated(), IsOrderParticipant()]

        return [IsAuthenticated()]

    def perform_create(self, serializer):
        serializer.save(client=self.request.user, status='pending')
