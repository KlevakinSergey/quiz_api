from django.contrib.auth import get_user_model

from rest_framework import generics
from .serializers import UserCreateSerializer


User = get_user_model()


class UserCreateView(generics.CreateAPIView):
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()

