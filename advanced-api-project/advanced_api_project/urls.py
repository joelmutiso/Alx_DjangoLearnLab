from django.urls import path
from .views import BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView

urlpatterns = [
    # Path for retrieving all books
    path('books/', BookListView.as_view(), name='book-list'),

    # Path for creating a new book
    path('books/create/', BookCreateView.as_view(), name='book-create'),

    # Path for retrieving, updating, or deleting a specific book
    # The <int:pk> captures the book's primary key (ID)
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('books/<int:pk>/update/', BookUpdateView.as_view(), name='book-update'),
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),
]
