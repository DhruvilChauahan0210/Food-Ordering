from django.contrib import admin
from django.urls import path, include
from products.views import homepage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name='homepage'),  # Add this line
    path('products/', include('products.urls')),
]
