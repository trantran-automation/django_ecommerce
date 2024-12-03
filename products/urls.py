# products/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.store_page, name='store'),
    path('product/product_detail/<int:product_id>/', views.product_detail, name='product_detail'),
    path('product/create/', views.product_create, name='product_create'),  
]
