from django.urls import path
from . import views

urlpatterns = [
    path('categories/',views.CategoryListCreateAPIView.as_view(),name='categories'),
    path('categories/<int:pk>/',views.CategoryRetrieveUpdateDestroyAPIView.as_view(),name='categories-details'),
    path('food-items/',views.FoodListCreateView.as_view(),name='food-items'),
    path('food-items/<int:pk>/',views.FoodRetrieveUpdateDestroyAPIView.as_view(),name='food-items-details'),
    path('add/cart/',views.AddToCartView.as_view(),name="add-to-cart"),
    path('cart/items/<int:pk>/',views.UpdateCartItemView.as_view(),name='update-cart'),
    path('cart/items/<int:pk>/remove/',views.RemoverCartView.as_view(),name='remove-cart'),
    path('cart/',views.CartView.as_view(),name='carts'),
]