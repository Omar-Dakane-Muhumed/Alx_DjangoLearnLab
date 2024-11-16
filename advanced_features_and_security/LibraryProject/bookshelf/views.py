from django.shortcuts import render
from django.contrib.auth.decorators import permission_required

# Create your views here.

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_view(request, pk):
    pass


["book_list", "raise_exception", "books"]



    from .forms import BookSearchForm

def search_books(request):
    if request.method == 'POST':
        form = BookSearchForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            books = Book.objects.filter(title__icontains=title)
        else:
            books = Book.objects.none()
    return render(request, 'bookshelf/book_list.html', {'books': books})
