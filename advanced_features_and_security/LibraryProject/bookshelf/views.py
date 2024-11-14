from django.shortcuts import render
from django.contrib.auth.decorators import permission_required

# Create your views here.

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_view(request, pk):
    pass


["book_list", "raise_exception", "books"]




# Secure version using Django ORM
from .models import Book

def search_books(request):
    title = request.GET.get('title', '')
    books = Book.objects.filter(title__icontains=title)  # 'icontains' for case-insensitive partial matching
    return render(request, 'bookshelf/book_list.html', {'books': books})