from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class FoodItems(models.Model):
    FOOD_CHOICES = [
        ('V','Vegetarian'),
        ('NV','Non-Vegetarian')
    ]

    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='food_items')
    food_type = models.CharField(max_length=2,choices=FOOD_CHOICES,default='V')
    image = models.URLField(max_length=500,null=True,blank=True)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['category']),
            models.Index(fields=['food_type']),
            models.Index(fields=['price']),
        ]

    def __str__(self):
        return self.name 

class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def total_price(self):
        return sum(items.total_price for items in self.items.all())

    def __str__(self):
        return f'cart: {self.user.email}'


class CartItem(models.Model):
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE,related_name='items')
    food_item = models.ForeignKey(FoodItems,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('cart','food_item')

    @property
    def total_price(self):
        return self.food_item.price * self.quantity
    
    def __str__(self):
        return f'{self.quantity} : {self.food_item.name} in cart'
