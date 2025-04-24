from django.urls import path
from . import views

urlpatterns = [
    path('categories/',views.CategoryListCreateAPIView.as_view(),name='categories'),
    path('categories/<int:pk>/',views.CategoryRetrieveUpdateDestroyAPIView.as_view(),name='categories-details'),
    path('food-items/',views.FoodListCreateView.as_view(),name='food-items'),
    path('food-items/<int:pk>/',views.FoodRetrieveUpdateDestroyAPIView.as_view(),name='food-items-details'),
]