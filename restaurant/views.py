from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView,GenericAPIView,UpdateAPIView,DestroyAPIView,RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from .serializer import CategorySerializer,FoodItemSerializer,AddToCartSerializer,UpdateCartItemSerializer,CartSerailizer
from .models import Category,FoodItems,Cart,CartItem
from rest_framework.response import Response

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

class AddToCartView(GenericAPIView):
    serializer_class = AddToCartSerializer
    permission_classes = [IsAuthenticated]

    def post(self,request,*args,**kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        cart,created = Cart.objects.get_or_create(user=request.user)
        food_item_id = serializer.validated_data['food_item_id']
        quantity = serializer.validated_data['quantity']

        cart_item,created = CartItem.objects.get_or_create(cart=cart,food_item_id=food_item_id,defaults={'quantity':quantity})

        if not created:
            cart_item.quantity += quantity
            cart_item.save()

        return Response({'detail':'items added to cart successfully'},status=status.HTTP_200_OK)
    

class UpdateCartItemView(UpdateAPIView):
    serializer_class = UpdateCartItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        cart,created = Cart.objects.get_or_create(user=self.request.user)
        return CartItem.objects.filter(cart=cart)
    
    def perform_update(self, serializer):
        if serializer.validated_data['quantity'] <= 0:
            self.get_object().delete()
        else:
            serializer.save()

class RemoverCartView(DestroyAPIView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        cart,created = Cart.objects.get_or_create(user=self.request.user)
        return CartItem.objects.filter(cart=cart)

class CartView(RetrieveAPIView):
    serializer_class = CartSerailizer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        cart,created = Cart.objects.get_or_create(user=self.request.user)
        return cart 