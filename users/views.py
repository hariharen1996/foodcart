from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from . import serializers

# Create your views here.
class CreateUserView(CreateAPIView):
    serializer_class = serializers.UserSerializer
    permission_classes = [AllowAny]