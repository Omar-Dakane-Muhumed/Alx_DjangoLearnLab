#retreive the book

book = Book.objects.get(title="1984") book.title, book.author, book.publication_year 
print(book)
# Expected output: ('1984', 'George Orwell', 1949)

