from django.contrib import admin
from .models import Book
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # fields to show in list view
    search_fields = ('title', 'author')  # adds a search box
    list_filter = ('publication_year',)  # adds a filter sidebar

# Register the Book model with this custom admin
admin.site.register(Book, BookAdmin)