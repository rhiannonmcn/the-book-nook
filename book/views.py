from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Book


class HomeList(generic.ListView):
    """_summary_

    Args:
        generic (_type_): _description_
    """
    model = Book
    queryset = Book.objects.filter(book_approved=True).order_by('?')
    template_name = 'index.html'


class BookList(generic.ListView):
    """_summary_

    Args:
        generic (_type_): _description_
    """
    model = Book
    queryset = Book.objects.filter(
        book_approved=True).order_by('-book_created_on')
    template_name = 'book/bookshelf.html'
    paginate_by = 18


class BookDetails(View):
    """_summary_

    Args:
        View (_type_): _description_
    """
    def get(self, request, slug, *args, **kwargs):
        """_summary_

        Args:
            request (_type_): _description_
            slug (_type_): _description_

        Returns:
            _type_: _description_
        """
        queryset = Book.objects.filter(book_approved=True)
        book = get_object_or_404(queryset, slug=slug)
        reviews = book.reviews.filter(
            review_approved=True).order_by('-review_created_on')

        return render(
            request,
            'book/book.html',
            {
                'book': book,
                'reviews': reviews
            },
        )
