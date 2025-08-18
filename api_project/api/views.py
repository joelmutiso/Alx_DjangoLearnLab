from rest_framework import generics
from .models import Books
from .serializers import BooksSerializer    

class BookList(generics.ListAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
