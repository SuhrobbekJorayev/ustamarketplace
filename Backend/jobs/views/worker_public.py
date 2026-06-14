from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import AllowAny
from jobs.models import User
from jobs.serializers import WorkerPublicSerializer


class WorkerPublicViewSet(ReadOnlyModelViewSet):
    queryset = User.objects.filter(role='worker')
    serializer_class = WorkerPublicSerializer

    permission_classes = [AllowAny]
