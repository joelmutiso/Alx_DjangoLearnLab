from rest_framework import serializers
from .models import Author, Book
from datetime import date

# Serializer for the Book model.
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

    def validate_publication_year(self, value):
        # Validation: Prevents saving a publication year in the future.
        if value > date.today().year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

# Serializer for the Author model.
class AuthorSerializer(serializers.ModelSerializer):
    # This nested field handles the one-to-many relationship, serializing all of an author's books.
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']