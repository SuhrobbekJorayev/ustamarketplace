from rest_framework.viewsets import generics
from rest_framework.permissions import IsAuthenticated
from jobs.serializers import WorkerProfileSerializer


class WorkerProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = WorkerProfileSerializer

    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user.worker_profile
