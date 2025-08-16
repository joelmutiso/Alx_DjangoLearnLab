import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_models.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def create_sample_data():
    """
    Creates sample data to test the queries.
    """
    print("Creating sample data...")

    # Create Authors
    author1 = Author.objects.create(name="Stephen King")
    author2 = Author.objects.create(name="J.K. Rowling")

    # Create Books and link them to authors (ForeignKey)
    book1 = Book.objects.create(title="The Shining", author=author1)
    book2 = Book.objects.create(title="It", author=author1)
    book3 = Book.objects.create(title="Harry Potter and the Sorcerer's Stone", author=author2)

    # Create Libraries
    library1 = Library.objects.create(name="Public Library")
    library2 = Library.objects.create(name="Community Library")

    # Add books to libraries (ManyToManyField)
    library1.books.add(book1, book3)
    library2.books.add(book2)

    # Create Librarians and link them to libraries (OneToOneField)
    librarian1 = Librarian.objects.create(name="Jane Doe", library=library1)
    librarian2 = Librarian.objects.create(name="John Smith", library=library2)
    
    print("Sample data created successfully!")

def run_queries():
    """
    Runs the specified queries to demonstrate ORM relationships.
    """
    print("\n--- Running Queries ---")

    # 1. Query all books by a specific author
    # This query uses the reverse relationship `author.book_set.all()`
    try:
        author = Author.objects.get(name="Stephen King")
        books = author.book_set.all()
        print(f"\nAll books by {author.name}:")
        for book in books:
            print(f"- {book.title}")
    except Author.DoesNotExist:
        print("\nAuthor 'Stephen King' not found.")

    # 2. List all books in a library
    # This query uses the `ManyToManyField` field name `library.books.all()`
    try:
        library = Library.objects.get(name="Public Library")
        books = library.books.all()
        print(f"\nAll books in {library.name}:")
        for book in books:
            print(f"- {book.title}")
    except Library.DoesNotExist:
        print("\nLibrary 'Public Library' not found.")
    
    # 3. Retrieve the librarian for a library
    # This query uses the `OneToOneField` field name `library.librarian`
    try:
        library = Library.objects.get(name="Community Library")
        librarian = library.librarian
        print(f"\nLibrarian for {library.name}: {librarian.name}")
    except Library.DoesNotExist:
        print("\nLibrary 'Community Library' not found.")
    except Librarian.DoesNotExist:
        print("\nNo librarian found for 'Community Library'.")


if __name__ == '__main__':
    # You may want to uncomment the lines below to clear the database
    # before creating new data if you run the script multiple times.
    # Author.objects.all().delete()
    # Book.objects.all().delete()
    # Library.objects.all().delete()
    # Librarian.objects.all().delete()

    create_sample_data()
    run_queries()