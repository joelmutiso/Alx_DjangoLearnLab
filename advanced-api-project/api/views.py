from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Book

class BookListView(ListView):
    """
    A view to retrieve a list of all books.
    """
    model = Book
    queryset = Book.objects.all()

class BookDetailView(DetailView):
    """
    A view to retrieve a single book by its ID.
    """
    model = Book

class BookCreateView(CreateView):
    """
    A view to create a new book.
    """
    model = Book
    fields = ['title', 'publication_year', 'author']

class BookUpdateView(UpdateView):
    """
    A view to update an existing book.
    """
    model = Book
    fields = ['title', 'publication_year', 'author']

class BookDeleteView(DeleteView):
    """
    A view to delete a book.
    """
    model = Book
    success_url = '/books/'