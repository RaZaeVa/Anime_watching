from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .serislizers import *
from rest_framework.permissions import IsAdminUser


class UserCreateView(APIView):

    def post(self, request):

        serializer = UserCreateSerializer(data=request.data, context={'request': request})

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(status.HTTP_400_BAD_REQUEST)


class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]