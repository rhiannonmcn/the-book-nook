from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Book
from .forms import BookForm


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
        favourite = False
        if book.book_favourites.filter(id=self.request.user.id).exists():
            favourite = True

        return render(
            request,
            'book/book.html',
            {
                'book': book,
                'reviews': reviews,
                'reviewed': False,
                'favourite': favourite,
                'review_form': BookForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
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
        favourite = False
        if book.book_favourites.filter(id=self.request.user.id).exists():
            favourite = True
        
        review_form = BookForm(data=request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review_form.instance.review_username = request.user
            review_form.instance.book_listing = book
            review.book = book
            review.save()

        else:
            review_form = BookForm()

        return render(
            request,
            'book/book.html',
            {
                'book': book,
                'reviews': reviews,
                'reviewed': True,
                'favourite': favourite,
                'review_form': review_form
            },
        )

   
class BookFavourite(View):
    """_summary_

    Args:
        View (_type_): _description_
    """
    def post(self, request, slug, *args, **kwargs):
        """_summary_

        Args:
            request (_type_): _description_
            slug (_type_): _description_

        Returns:
            _type_: _description_
        """
        book = get_object_or_404(Book, slug=slug)
        
        if book.book_favourites.filter(id=request.user.id).exists():
            book.book_favourites.remove(request.user)
        else:
            book.book_favourites.add(request.user)
            
        return HttpResponseRedirect(reverse('book_detail', args=[slug]))
