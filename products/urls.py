from django.urls import path
from .views import product_list, product_detail, product_create, product_update, product_delete

urlpatterns = [
    path('', product_list, name='product_list'),
    path('<uuid:pk>/', product_detail, name='product_detail'),
    path('new/', product_create, name='product_create'),
    path('<uuid:pk>/edit/', product_update, name='product_update'),
    path('<uuid:pk>/delete/', product_delete, name='product_delete'),
]
