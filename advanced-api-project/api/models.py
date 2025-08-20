from django.db import models

# Model to represent an Author.
class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

# Model to represent a Book.
class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    # ForeignKey links a Book to a single Author. If the author is deleted, so are their books.
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title