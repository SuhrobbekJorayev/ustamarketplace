from rest_framework import viewsets
from jobs.models import WorkerProfile
from jobs.serializers import WorkerProfileSerializer


class WorkerProfileViewSet(viewsets.ModelViewSet):
    queryset = WorkerProfile.objects.all()
    serializer_class = WorkerProfileSerializer

    def get_queryset(self):
        return WorkerProfile.objects.filter(id=self.request.user)
