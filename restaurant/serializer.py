from rest_framework import serializers
from .models import Category,FoodItems,Cart,CartItem

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
    
class AddToCartSerializer(serializers.Serializer):
    food_item_id = serializers.IntegerField()
    quantity = serializers.IntegerField(default=1)

    def validate_food_items_id(self, attrs):
        if not FoodItems.objects.filter(pk=attrs).exists():
            raise serializers.ValidationError('food items does not exists')
        return attrs
    
    def save(self, **kwargs):
        user = self.context['request'].user
        food_item_id = self.validated_data['food_item_id']
        quantity = self.validated_data['quantity']

        cart,_ = Cart.objects.create(user=user)
        cart_item,created = CartItem.objects.create(cart=cart,food_item_id=food_item_id,defaults={'quantity':quantity})
        if not created:
            cart_item.quantity += quantity 
            cart_item.save()
        
        return cart
    
class UpdateCartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['quantity']

class CartItemSerializer(serializers.ModelSerializer):
    food_item = FoodItemSerializer(read_only=True)
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = CartItem
        fields = ['id','food_item','quantity','total_price']
        read_only_fields = ('total_price',)
    
    def get_total_price(self,data):
        return data.total_price

class CartSerailizer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True,read_only=True)
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ['id','items','total_price','created_at','updated_at']
        read_only_fields = ('user','total_price')
    
    def get_total_price(self,data):
        return data.total_price 