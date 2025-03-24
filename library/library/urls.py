from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
# from books.views import admin_dashboard

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('books.urls')),
]
