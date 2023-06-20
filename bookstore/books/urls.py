from django.urls import path

from books import views

app_name = 'books'

urlpatterns = [
    path('', views.index, name='index'),
    path('books/<int:id>/', views.books_detail, name='books_detail'),
    path('category/<slug:category_slug>/', views.category_books,
         name='category_books'),
    path('author/<slug:author_slug>/', views.author_books,
         name='author_books'),
    path('publisher/<slug:publisher_slug>/', views.publisher_books,
         name='publisher_books'),
    path('books/new/', views.book_new, name='book_new'),
]
