from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from django.views.decorators.csrf import csrf_protect
from .models import Book
from .forms import SearchForm
from .forms import ExampleForm

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    form = SearchForm(request.GET or None)
    books = Book.objects.all()

    if form.is_valid():
        q = form.cleaned_data.get("query")
        if q:
            
            books = books.filter(title__icontains=q)

    return render(request, 'bookshelf/book_list.html', {'books': books, 'form': form})


list_books = book_list

@csrf_protect
@permission_required('bookshelf.can_create', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        title = (request.POST.get('title') or "").strip()
        author = (request.POST.get('author') or "").strip()
        published_date = (request.POST.get('published_date') or "").strip()

        if title and author and published_date:
            Book.objects.create(title=title, author=author, published_date=published_date)
            return redirect('book_list')

    return render(request, 'bookshelf/form_example.html', {'action': 'add'})

@csrf_protect
@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if request.method == 'POST':
        title = (request.POST.get('title') or "").strip()
        author = (request.POST.get('author') or "").strip()
        published_date = (request.POST.get('published_date') or "").strip()

        if title:
            book.title = title
        if author:
            book.author = author
        if published_date:
            book.published_date = published_date

        book.save()
        return redirect('book_list')

    return render(request, 'bookshelf/form_example.html', {'action': 'edit', 'book': book})

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':  
        book.delete()
        return redirect('book_list')
    return render(request, 'bookshelf/form_example.html', {'action': 'delete', 'book': book})

