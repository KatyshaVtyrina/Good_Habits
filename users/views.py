from django.contrib.auth.hashers import make_password
from rest_framework import generics

from users.serializers import UserSerializer


class UserRegisterApiView(generics.CreateAPIView):

    serializer_class = UserSerializer

    def perform_create(self, serializer):
        """Хеширование пароля"""
        password = serializer.validated_data['password']
        serializer.save(password=make_password(password))
