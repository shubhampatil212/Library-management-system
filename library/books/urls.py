from django.urls import path
from .views import book_list

urlpatterns = [
    path('', book_list, name='book-list'),  # Show book list to users
]
