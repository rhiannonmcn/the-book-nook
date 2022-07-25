from . import views
from django.urls import path


urlpatterns = [
    path('', views.HomeBookList.as_view(), name='home'),
    path('bookshelf/', views.BookList.as_view(), name='book_shelf'),
    path('<slug:slug>', views.BookDetails.as_view(), name='book_detail' )
]