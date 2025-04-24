from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from .serializer import CategorySerializer,FoodItemSerializer
from .models import Category,FoodItems

# Create your views here.
class CategoryListCreateAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]    

class CategoryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

class FoodListCreateView(ListCreateAPIView):
    queryset = FoodItems.objects.select_related('category').all()
    serializer_class = FoodItemSerializer
    permission_classes = [IsAuthenticated]

class FoodRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = FoodItems.objects.select_related('category').all()
    serializer_class = FoodItemSerializer
    permission_classes = [IsAuthenticated]