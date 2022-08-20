from . import views
from django.urls import path


urlpatterns = [
    path('', views.HomeList.as_view(), name='home'),
    path('bookshelf/', views.BookList.as_view(), name='book_shelf'),
    path('<slug:slug>', views.BookDetails.as_view(), name='book_detail' ),
    path('genre/<slug:slug>', views.GenreDetail.as_view(), name='genre_detail' ),
    path('favourite/<slug:slug>', views.BookFavourite.as_view(), name='book_favourite'),
    path('add_book/', views.AddBook.as_view(), name='add_book'),
    path('my_books/', views.MyBooks.as_view(), name='my_books'),
    path('<int:pk>/edit_review/', views.EditReview.as_view(), name='edit_review' ),
    path('<int:pk>/delete_review/', views.DeleteReview.as_view(), name='delete_review' ),
    path('contact/', views.Contact.as_view(), name='contact' ),
    path('approvals/', views.AdminOnly.as_view(), name='admin_only' ),
    path('<int:pk>/approve_book/', views.EditBookListing.as_view(), name='edit_book_listing' ),
    path('<int:pk>/approve_review/', views.ApproveReview.as_view(), name='approve_review' ),
    path('<int:pk>/', views.DeleteBook.as_view(), name='delete_book_admin' ),
]