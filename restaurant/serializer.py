from rest_framework import serializers
from .models import Category,FoodItems

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category 
        fields = ["id",'name','description','created_at','updated_at']
        read_only_fields = ('created_at','updated_at')

class FoodItemSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())

    class Meta:
        model = FoodItems
        fields = '__all__'
        read_only_fields = ('created_at','updated_at')