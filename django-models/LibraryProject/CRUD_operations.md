## Create
```python
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book
# Output:
# <Book: 1984>

from bookshelf.models import Book
books = Book.objects.all()
for book in books:
    print(book.title, book.author, book.publication_year)

# Output:
# 1984 George Orwell 1949

book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
book
# Output:
# <Book: Nineteen Eighty-Four>

book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# Check deletion
Book.objects.all()
# Output:
# <QuerySet []>







