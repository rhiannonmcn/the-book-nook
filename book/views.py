from django.shortcuts import render, get_object_or_404, reverse
from django.views.generic import View, CreateView, ListView
from django.http import HttpResponseRedirect
from django.utils.text import slugify
from .models import Book, Genre
from .forms import AddBookForm, BookForm


class HomeList(ListView):
    
    model = Book
    template_name = 'index.html'
    queryset = Book.objects.filter(book_approved=True).order_by('?')
    
    def get_context_data(self, **kwargs):
        """_summary_

        Returns:
            _type_: _description_
        """
        context_data = super().get_context_data(**kwargs)
        context_data['genre_list'] = Genre.objects.all()
        return context_data


class BookList(ListView):
    """_summary_

    Args:
        generic (_type_): _description_
    """
    model = Book
    queryset = Book.objects.filter(
        book_approved=True).order_by('-book_created_on')
    template_name = 'book/bookshelf.html'
    paginate_by = 18
    

class AddBook(CreateView):
    """_summary_

    Args:
        generic (_type_): _description_
    """
    template_name = 'book/add_book.html'
    form_class = AddBookForm
    queryset = Book.objects.all()
    get_context_object_name = 'book_form'
    
    
    def form_valid(self, form):
        form = form.save(commit=False)
        form.slug = slugify(form.title + "-" + form.book_author)
        return(super().form_valid(form))

            

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
    
    
class GenreDetail(View):
        
    def get(self, request, slug, *args, **kwargs):
    
        genre_object = Genre.objects.all()
        genres = get_object_or_404(genre_object, slug=slug)
        books = genres.book_genre.filter(
            book_approved=True).order_by('-book_created_on')
        

        return render(
            request,
            'book/genre.html',
            {
                'books': books,
                'genres': genres,
                'genre_object':genre_object
            },
        )
