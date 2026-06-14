from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework import viewsets, views, mixins
from jobs.models import (
    Category,
    User,
    WorkerProfile,
    Service,
    Order,
    Review
)
from dashboard.serializers import (
    AdminCategorySerializer,
    AdminUserSerializer,
    AdminWorkerProfileSerializer,
    AdminServiceSerializer,
    AdminOrderSerializer,
    AdminReviewSerializer
)


class AdminCategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = AdminCategorySerializer

    permission_classes = [IsAdminUser]


class AdminUserViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = AdminUserSerializer

    permission_classes = [IsAdminUser]


class AdminWorkerProfileViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = WorkerProfile.objects.all()
    serializer_class = AdminWorkerProfileSerializer

    permission_classes = [IsAdminUser]


class AdminServiceViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = Service.objects.all()
    serializer_class = AdminServiceSerializer

    permission_classes = [IsAdminUser]


class AdminOrderViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = Order.objects.all()
    serializer_class = AdminOrderSerializer

    permission_classes = [IsAdminUser]


class AdminReviewViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = Review.objects.all()
    serializer_class = AdminReviewSerializer

    permission_classes = [IsAdminUser]


class AdminDashboardStatsView(views.APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        data = {
            'users': User.objects.count(),
            'workers': User.objects.filter(role='worker').count(),
            'services': Service.objects.count(),
            'orders': Order.objects.count(),
            'reviews': Review.objects.count(),
            'categories': Category.objects.count(),
            'worker_profiles': WorkerProfile.objects.count(),
        }

        return Response(data)
