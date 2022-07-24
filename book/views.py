from re import template
from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Book



class BookList(generic.ListView):
    model = Book
    queryset = Book.objects.filter(book_approved=True).order_by('-book_created_on')
    template_name = 'book/bookshelf.html'
    paginate_by = 18

    
class BookDetails(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Book.objects.filter(book_approved=True)
        book = get_object_or_404(queryset, slug=slug)
        reviews = book.reviews.filter(review_approved=True).order_by('-review_created_on')
   
        return render(
            request,
            'book/book.html',
            {
                'book': book,
                'reviews': reviews
            },
        )
