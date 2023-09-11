from django.shortcuts import get_object_or_404, redirect, render

from books.forms import BookForm
from books.models import Author, Book, Category, Publisher


def index(request):
    book_list = Book.objects.select_related(
        'category',
        'author',
        'publisher',
    ).filter(
        is_published=True,
        category__is_published=True,
    )
    context = {
        'book_list': book_list,
    }
    return render(request, 'books/index.html', context)


def books_detail(request, id):
    book = get_object_or_404(
        Book.objects.select_related(
            'category',
            'author',
            'publisher',
        ).filter(
            is_published=True,
            category__is_published=True,
        ), id=id
    )
    context = {
        'book': book,
    }
    return render(request, 'books/detail.html', context)


def category_books(request, category_slug):
    category = get_object_or_404(
        Category.objects.filter(
            is_published=True,
            slug=category_slug,
        )
    )
    book_list = category.books.filter(
        is_published=True,
    )
    context = {
        'book_list': book_list,
        'category': category,
    }
    return render(request, 'books/category.html', context)


def author_books(request, author_slug):
    author = get_object_or_404(
        Author.objects.filter(
            slug=author_slug,
        )
    )
    book_list = author.books.filter(
        is_published=True,
    )
    context = {
        'book_list': book_list,
        'author': author,
    }
    return render(request, 'books/author.html', context)


def publisher_books(request, publisher_slug):
    publisher = get_object_or_404(
        Publisher.objects.filter(
            slug=publisher_slug,
        )
    )
    book_list = publisher.books.filter(
        is_published=True,
    )
    context = {
        'book_list': book_list,
        'publisher': publisher,
    }
    return render(request, 'books/publisher.html', context)


def book_new(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save()
            book.save()
            return redirect('books:books_detail', id=book.id)
    else:
        form = BookForm()
    return render(request, 'books/book_new.html', {'form': form})
