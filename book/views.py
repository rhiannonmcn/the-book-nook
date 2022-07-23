from django.shortcuts import render
from django.views import generic
from .models import Book



class BookList(generic.ListView):
    model = Book
    queryset = Book.objects.filter(book_approved=True).order_by('-book_created_on')
    template_name = 'book/bookshelf.html'
    paginate_by = 18
