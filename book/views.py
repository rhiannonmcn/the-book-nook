from django.shortcuts import render, get_object_or_404, reverse
from django.views.generic import (
    View, CreateView, ListView, UpdateView, DeleteView, TemplateView
    )
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.utils.text import slugify
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Book, BookReview, Genre
from .forms import AddBookForm, BookForm
from django.contrib.auth.mixins import UserPassesTestMixin


class HomeList(ListView):
    """
    Takes the book object from Book model
    and returns a list of those with approved
    = True and in random order on the home page
    """

    model = Book
    template_name = 'index.html'
    queryset = Book.objects.filter(book_approved=True).exclude(
        book_image__icontains='placeholder').order_by('?')

    def get_context_data(self, **kwargs):
        """
        Takes the genre object from Genre model
        and returns a list
        """
        context_data = super().get_context_data(**kwargs)
        context_data['genre_list'] = Genre.objects.all()
        return context_data


class BookList(ListView):
    """
    Takes the book object from Book model
    and returns a list of those with approved
    = True and in order of when they were created
    in the Bookshelf page
    """
    model = Book
    queryset = Book.objects.filter(
        book_approved=True).order_by('-book_created_on')
    template_name = 'book/bookshelf.html'
    paginate_by = 8
    context_object_name = 'bookshelf'

    def get_queryset(self):
        """
        Gets the user input in the search field
        in the template and returns a list of books
        from the Book model filtered by title,
        book_author and book_blurb and the book
        has approved = True
        """
        name = self.request.GET.get('search', '')
        object_list = Book.objects.filter(book_approved=True)
        if name:
            object_list = object_list.filter(
                Q(title__icontains=name) | Q(book_author__icontains=name) |
                Q(book_blurb__icontains=name))
        return object_list


class AddBook(LoginRequiredMixin, CreateView):
    """
    This view makes sure the user is logged in
    before they can access the template

    Calls the AddBookForm from forms.py to add
    a book to the database
    """
    template_name = 'book/add_book.html'
    form_class = AddBookForm

    def get_success_url(self):
        """
        sets the reverse url for the
        successful addition of the book
        to the database
        """
        return reverse('book_shelf')

    def form_valid(self, form):
        """_summary_
        validates the form and adds a success message
        to the template once abook is successfully added
        Sets the automatic slug for the object created
        from the user input on the title and book author
        fields
        """
        form = form.save(commit=False)
        messages.success(
            self.request,
            'You have added a new book and it has been flagged for approval!')
        form.slug = slugify(form.title + "-" + form.book_author)
        return super().form_valid(form)


class BookDetails(View):
    """
    Displays the full individual book object from
    Book model as well as the reviews associated
    with the book object and the bookmark status
    for the object
    """

    def get(self, request, slug, *args, **kwargs):
        """
        Gets full book detail with approved reviews
        Checks if the book is bookmarked by the current user
        Current user can bookmark/un-bookmark a book
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
        """
        Gets full book detail with approved reviews
        Checks if the book is bookmarked by the current user
        Current user can bookmark/un-bookmark a book
        Current user can submit a review form for approval

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


class BookmarkBook(View):
    """
    Users can bookmark or un-bookmark a book object
    """

    def post(self, request, slug, *args, **kwargs):
        """
        Gets the specific book instance from Book model
        Checks if the user is attached to the book object
        and adds or removes the user which will be called
        via template book_detail
        """
        book = get_object_or_404(Book, slug=slug)

        if book.book_favourites.filter(id=request.user.id).exists():
            book.book_favourites.remove(request.user)
        else:
            book.book_favourites.add(request.user)

        return HttpResponseRedirect(reverse('book_detail', args=[slug]))


class GenreDetail(View):
    """
    Returns all the book objects from the Book model
    filtered by a genre and with book_approved = True
    """

    def get(self, request, slug, *args, **kwargs):
        """
        Get all the genre objects from the Genre model
        and the specific slug of the genre object
        Gets all the book objects filtered then by
        their genre with book_approved = True
        returns the single genre object instance,
        the book object and the genre object list
        """

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
                'genre_object': genre_object
            },
        )


class MyBooks(LoginRequiredMixin, CreateView):
    """
    Gets all the current users bookmarked books
    and all the user's reviews and displays them
    on the template
    If the user is logged in the my_books template
    can be accessed

    """

    def get(self, request, *args, **kwargs):
        """
        Establishes the current user
        Gets all the books where book_favourites =
        current user
        Gets all the reviews where the review_username =
        current user
        returns the user book favourites and user reviews
        and the current user username
        """
        username = request.user
        user_fav = Book.objects.filter(book_favourites=request.user)
        user_review = BookReview.objects.filter(review_username=username)
        return render(
            request, 'book/my_books.html', {
                'user_fav': user_fav,
                'user_review': user_review,
                'username': username,
            })


class EditReview(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    """
    Logged in user can edit any reviews they have made
    which will then be sent to be approved again
    template is edit_review.html
    reverse url is my_books.html
    """

    model = BookReview
    fields = [
        'review_detail',
    ]
    template_name = 'book/edit_review.html'
    success_url = reverse_lazy('my_books')
    success_message = "You have updated your review and \
    it has been flagged for approval!"

    def get_context_data(self, **kwargs):
        """
        Get the object instance's book title
        """
        context = super().get_context_data(**kwargs)
        context['book_title'] = self.object.book_listing

        return context

    def form_valid(self, form):
        """
        Validate form
        Set the review_approved status to False
        Save and return the new object
        """
        form.instance.review_approved = False
        form.save()
        return super().form_valid(form)


class DeleteReview(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    """
    Delete the current's user's review
    template is delete_review.html
    reverse url is my_books.html
    """
    model = BookReview
    success_url = reverse_lazy('my_books')
    success_message = "Review successfully deleted!"
    template_name = 'book/delete_review.html'

    def get_context_data(self, **kwargs):
        """
        Get and return the object instance book_title,
        review_detail, current user's username,
        review date created on
        """
        context = super().get_context_data(**kwargs)
        context['book_title'] = self.object.book_listing
        context['review_detail'] = self.object.review_detail
        context['user'] = self.object.review_username
        context['date'] = self.object.review_created_on

        return context


class Contact(TemplateView):
    """
    returns the contact.html template
    """
    template_name = 'contact.html'


class AdminOnly(UserPassesTestMixin, ListView):
    """
    Checks that the user is a superuser only
    Gets a list of books from Book model with
    book_approved = False
    Gets a list of reviews from BookReview
    model with review_approved = False
    template is admin_only.html
    """

    def test_func(self):
        """
        Checks if the current user is
        a superuser and allows access to
        the template if they are
        """
        return self.request.user.is_superuser

    template_name = 'admin_only.html'
    model = Book
    queryset = Book.objects.filter(
        book_approved=False).order_by('-book_created_on')
    context_object_name = 'for_approval'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        """
        Gets the review from the BookReview model
        with the review_approved = False
        """
        context = super().get_context_data(**kwargs)
        context['reviews'] = BookReview.objects.filter(
            review_approved=False).order_by('-review_created_on')
        return context


class EditBookListing(UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    """
    Checks the user is a superuser only
    Gets the book object instance from
    Book model and allows the superuser
    to update the book object
    template is approve_book.html
    """

    model = Book
    fields = [
        'title',
        'book_author',
        'book_blurb',
        'book_genre',
    ]
    template_name = 'approve_book.html'
    success_url = reverse_lazy('admin_only')
    success_message = "You approved the book"

    def test_func(self):
        """
        Checks if the current user is
        a superuser and allows access to
        the template if they are
        """
        return self.request.user.is_superuser

    def form_valid(self, form):
        """
        Validate form
        Set the book_approved status to True
        Save and return the new object
        """
        form.instance.book_approved = True
        form.save()
        return super().form_valid(form)


class ApproveReview(SuccessMessageMixin, UpdateView):
    """
    Gets the review object instance from
    BookReview model and allows the superuser
    to update the review object
    """

    model = BookReview
    fields = [
        'review_approved',
    ]
    success_url = reverse_lazy('admin_only')
    success_message = "You approved the review"

    def form_valid(self, form):
        """
        Validate form
        Set the review_approved status to True
        Save and return the new object
        """
        form.instance.review_approved = True
        form.save()
        return super().form_valid(form)


class DeleteBook(SuccessMessageMixin, DeleteView):
    """
    Gets the book object instance from
    Book model and allows the superuser
    to delet the book object
    """
    model = Book
    success_url = reverse_lazy('admin_only')
    success_message = "Book successfully deleted!"


class DeleteReviewAdmin(SuccessMessageMixin, DeleteView):
    """
    Gets the review object instance from
    BookReview model and allows the superuser
    to delete the review object
    """
    model = BookReview
    success_url = reverse_lazy('admin_only')
    success_message = "Book Review successfully deleted!"
