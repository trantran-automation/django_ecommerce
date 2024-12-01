# products/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.store_page, name='store'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),  
]
