"""
Sample queries demonstrating relationships between Author, Book, Library, and Librarian.
Run this script using:
    python manage.py shell < relationship_app/query_samples.py
"""

from relationship_app.models import Author, Library

# 1. Query all books by a specific author
author_name = "J.K. Rowling"
try:
    author = Author.objects.get(name=author_name)
    books_by_author = author.books.all()
    print(f"Books by {author_name}:")
    for book in books_by_author:
        print(f"- {book.title}")
except Author.DoesNotExist:
    print(f"No author found with name '{author_name}'.")

print("\n" + "-"*50 + "\n")

# 2. List all books in a library
library_name = "Central Library"
try:
    library = Library.objects.get(name=library_name)
    books_in_library = library.books.all()
    print(f"Books in {library_name}:")
    for book in books_in_library:
        print(f"- {book.title} (by {book.author.name})")
except Library.DoesNotExist:
    print(f"No library found with name '{library_name}'.")

print("\n" + "-"*50 + "\n")

# 3. Retrieve the librarian for a library
try:
    librarian = library.librarian
    print(f"The librarian at {library_name} is {librarian.name}.")
except Library.DoesNotExist:
    print(f"No library found with name '{library_name}'.")
except AttributeError:
    print(f"No librarian assigned to '{library_name}'.")
