from django.shortcuts import render
from django.contrib.auth.decorators import permission_required

# Create your views here.

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_view(request, pk):
    pass


["book_list", "raise_exception", "books"]