from django.shortcuts import render
from .models import Book

def book_list(request):
    books = Book.objects.all()  # Fetch all books
    return render(request, 'books/book_list.html', {'books': books})
