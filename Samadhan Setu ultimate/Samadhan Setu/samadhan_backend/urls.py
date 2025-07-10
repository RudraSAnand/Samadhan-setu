# samadhan_backend/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),     # Django admin
    path('', include('setu.urls')),      # Include all app routes
]
