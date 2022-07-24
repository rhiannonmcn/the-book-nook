from . import views
from django.urls import path


urlpatterns = [
    path('bookshelf/', views.BookList.as_view(), name='book_shelf'),
    path('<slug:slug>', views.BookDetails.as_view(), name='book_detail' )
]