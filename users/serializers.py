from django.contrib.auth import get_user_model 
from rest_framework import serializers
from rest_framework.authtoken.models import Token

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = ['id','username','email','password','phone','address']
        extra_kwargs = { 'password': { 'write_only': True } }
    
    def create(self,validated_data):
        user = User.objects.create(username=validated_data['username'],email=validated_data['email'],
                                password=validated_data['password'],phone=validated_data.get('phone',''),
                                address=validated_data.get('address',''))
        
        Token.objects.create(user=user)
        return user