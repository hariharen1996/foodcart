from django.shortcuts import render
from rest_framework.generics import CreateAPIView,GenericAPIView
from rest_framework.permissions import AllowAny,IsAuthenticated
from . import serializers
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class CreateUserView(CreateAPIView):
    serializer_class = serializers.UserSerializer
    permission_classes = [AllowAny]

class LoginView(ObtainAuthToken):
    serializer_class = serializers.AuthTokenSerializer

    def post(self, request, *args, **kwargs):
        serializers = self.serializer_class(data=request.data,context={'request':request})
        serializers.is_valid(raise_exception=True)
        user = serializers.validated_data['user']
        token,created = Token.objects.get_or_create(user=user)
        return Response({'token':token.key,'user_id':user.pk,'email':user.email})

class LogoutView(GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self,request,*args,**kwargs):
        print(request.user)
        request.user.auth_token.delete()
        print(request.user)
        return Response({'message':'you have been successfully logged out.'},status=status.HTTP_200_OK)