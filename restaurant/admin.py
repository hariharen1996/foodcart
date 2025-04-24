from django.contrib import admin
from .models import Category,FoodItems

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name','description','created_at','updated_at')
    search_fields = ('name',)
    ordering = ('created_at',)

@admin.register(FoodItems)
class FoodItemsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category', 'food_type', 'is_available', 'created_at')
    list_filter = ('name','price','category','food_type','is_available')
    search_fields = ('name',)
    list_editable = ('is_available',)
    ordering = ('-created_at',)
    