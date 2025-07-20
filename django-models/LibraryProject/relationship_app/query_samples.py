from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author using name
author_name = "George Orwell"
author = Author.objects.get(name=author_name)
books_by_author = Book.objects.filter(author=author)
print(f"Books by {author_name}:", books_by_author)

# List all books in a library using the library's name
library_name = "National Library"
library = Library.objects.get(name=library_name)
books_in_library = library.books.all()
print(f"Books in '{library_name}':", books_in_library)

# Retrieve the librarian for a library
librarian = Librarian.objects.get(library=library)
print(f"Librarian of '{library_name}':", librarian)
