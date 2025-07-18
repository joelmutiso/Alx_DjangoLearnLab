# CRUD Operations on the Book Model

This file documents the commands and outputs for Create, Retrieve, Update, and Delete operations performed via the Django shell.

---

## Create
**Command**: Create a Book instance with the title “1984”, author “George Orwell”, and publication year 1949.  
**Document in**: create.md  
**Expected Documentation**:
```python
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book
# <Book: 1984>
```
The Book instance was successfully created.

---

## Retrieve
**Command**: Retrieve and display all attributes of the book you just created.  
**Document in**: retrieve.md  
**Expected Documentation**:
```python
book = Book.objects.get(title="1984")
print(book.title, book.author, book.publication_year)
# 1984 George Orwell 1949
```

---

## Update
**Command**: Update the title of “1984” to “Nineteen Eighty-Four” and save the changes.  
**Document in**: update.md  
**Expected Documentation**:
```python
book.title = "Nineteen Eighty-Four"
book.save()
print(book.title)
# Nineteen Eighty-Four
```

---

## Delete
**Command**: Delete the book you created and confirm the deletion by trying to retrieve all books again.  
**Document in**: delete.md  
**Expected Documentation**:
```python
book.delete()
Book.objects.all()
# <QuerySet []>
```

---