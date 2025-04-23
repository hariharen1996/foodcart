from django.urls import path
from . import views

urlpatterns = [
    path('categories/',views.CategoryListCreateAPIView.as_view(),name='categories'),
    path('categories/<int:pk>/',views.CategoryRetrieveUpdateDestroyAPIView.as_view(),name='category-details'),   
]