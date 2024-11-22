

# api/serializers.py
from rest_framework import serializers
from .models import Book  # Assuming you have a Book model in the same app

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book  # Your Book model
        fields = '__all__'  # This includes all fields in the Book model
