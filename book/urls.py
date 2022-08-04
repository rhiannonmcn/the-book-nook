from . import views
from django.urls import path


urlpatterns = [
    path('', views.HomeList.as_view(), name='home'),
    path('bookshelf/', views.BookList.as_view(), name='book_shelf'),
    path('<slug:slug>', views.BookDetails.as_view(), name='book_detail' ),
    path('genre/<slug:slug>', views.GenreDetail.as_view(), name='genre_detail' ),
    path('favourite/<slug:slug>', views.BookFavourite.as_view(), name='book_favourite'),
    path('add_book/', views.AddBook.as_view(), name='add_book'),
    path('my_books/', views.MyBooks.as_view(), name='my_books')

]