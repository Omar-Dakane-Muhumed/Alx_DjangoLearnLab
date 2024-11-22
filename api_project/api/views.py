

from rest_framework.generics import ListAPIView
from .models import Book  # Import your Book model
from .serializers import BookSerializer  # Import the serializer

class BookList(ListAPIView):
    queryset = Book.objects.all()  # Query all book records
    serializer_class = BookSerializer  # Use the serializer
