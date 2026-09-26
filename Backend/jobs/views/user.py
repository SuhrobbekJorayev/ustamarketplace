from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser

from jobs.serializers import UserSerializer
from .imagekit import upload_avatar


class MeView(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

    def put(self, request):
        data = request.data.copy()

        avatar = request.FILES.get("avatar")

        if avatar:
            avatar_url = upload_avatar(avatar)
            data["avatar"] = avatar_url

        serializer = UserSerializer(
            request.user,
            data=data,
            partial=True
        )

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)
