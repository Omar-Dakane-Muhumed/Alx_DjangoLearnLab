# api/views.py
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()  # Retrieves all Book instances
    serializer_class = BookSerializer  # Uses the BookSerializer for serialization
