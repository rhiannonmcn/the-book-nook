from django.shortcuts import render, get_object_or_404, reverse
from django.views.generic import View, CreateView, ListView, UpdateView, DeleteView, FormView
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.utils.text import slugify
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Book, BookReview, Genre
from .forms import AddBookForm, BookForm, ContactForm
from django.contrib.auth.mixins import UserPassesTestMixin



class HomeList(ListView):
    """_summary_

    Args:
        ListView (_type_): _description_

    Returns:
        _type_: _description_
    """

    model = Book
    template_name = 'index.html'
    queryset = Book.objects.filter(book_approved=True).exclude(book_image__icontains='placeholder').order_by('?')

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
    paginate_by = 8
    context_object_name = 'bookshelf'

    def get_queryset(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        name = self.request.GET.get('search', '')
        object_list = Book.objects.filter(book_approved=True)
        if name:
            object_list = object_list.filter(
                Q(title__icontains=name) | Q(book_author__icontains=name)
                | Q(book_blurb__icontains=name))
        return object_list


class AddBook(LoginRequiredMixin, CreateView):
    """_summary_

    Args:
        generic (_type_): _description_
    """
    template_name = 'book/add_book.html'
    form_class = AddBookForm

    def get_success_url(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return reverse('book_shelf')

    def form_valid(self, form):
        """_summary_

        Args:
            form (_type_): _description_

        Returns:
            _type_: _description_
        """
        form = form.save(commit=False)
        messages.success(
            self.request,
            'You have added a new book and it has been flagged for approval!')
        form.slug = slugify(form.title + "-" + form.book_author)
        return super().form_valid(form)


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
    """_summary_

    Args:
        LoginRequiredMixin (_type_): _description_
        View (_type_): _description_

    """

    def get(self, request, *args, **kwargs):
        """_summary_

        Args:
            request (_type_): _description_

        Returns:
            _type_: _description_
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
    """_summary_

    Args:
        SuccessMessageMixin (_type_): _description_
        LoginRequiredMixin (_type_): _description_
        UpdateView (_type_): _description_
    """

    model = BookReview
    fields = [
        'review_detail',
    ]
    template_name = 'book/edit_review.html'
    success_url = reverse_lazy('my_books')
    success_message = "You have updated your review and it has been flagged for approval!"

    def get_context_data(self, **kwargs):
        """_summary_

        Returns:
            _type_: _description_
        """
        context = super().get_context_data(**kwargs)
        context['book_title'] = self.object.book_listing

        return context

    def form_valid(self, form):
        form.instance.review_approved = False
        form.save()
        return super().form_valid(form)


class DeleteReview(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    """_summary_

    Args:
        SuccessMessageMixin (_type_): _description_
        LoginRequiredMixin (_type_): _description_
        generic (_type_): _description_

    Returns:
        _type_: _description_
    """
    model = BookReview
    success_url = reverse_lazy('my_books')
    success_message = "Review successfully deleted!"
    template_name = 'book/delete_review.html'

    def get_context_data(self, **kwargs):
        """_summary_

        Returns:
            _type_: _description_
        """
        context = super().get_context_data(**kwargs)
        context['book_title'] = self.object.book_listing
        context['review_detail'] = self.object.review_detail
        context['user'] = self.object.review_username
        context['date'] = self.object.review_created_on

        return context


class Contact(SuccessMessageMixin, FormView):
    """_summary_

    Args:
        CreateView (_type_): _description_
    """

    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact')
    success_message = 'Thank you, your message has been sent and someone will be in contact with you as soon as possible!'


class AdminOnly(UserPassesTestMixin, ListView):
    """_summary_

    Args:
        View (_type_): _description_
    """

    def test_func(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.request.user.is_superuser

    template_name = 'admin_only.html'
    model = Book
    queryset = Book.objects.filter(
        book_approved=False).order_by('-book_created_on')
    context_object_name = 'for_approval'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        """_summary_

        Returns:
            _type_: _description_
        """
        context = super().get_context_data(**kwargs)
        context['reviews'] = BookReview.objects.filter(
            review_approved=False).order_by('-review_created_on')
        return context


class EditBookListing(SuccessMessageMixin, UpdateView):

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

    def form_valid(self, form):
        form.instance.book_approved = True
        form.save()
        return super().form_valid(form)


class ApproveReview(SuccessMessageMixin, UpdateView):

    model = BookReview
    fields = [
        'review_approved',
    ]
    success_url = reverse_lazy('admin_only')
    success_message = "You approved the review"

    def form_valid(self, form):
        form.instance.review_approved = True
        form.save()
        return super().form_valid(form)


class DeleteBook(SuccessMessageMixin, DeleteView):
    """_summary_

    Args:
        SuccessMessageMixin (_type_): _description_
        LoginRequiredMixin (_type_): _description_
        generic (_type_): _description_

    Returns:
        _type_: _description_
    """
    model = Book
    success_url = reverse_lazy('admin_only')
    success_message = "Book successfully deleted!"
    
    
class DeleteReviewAdmin(SuccessMessageMixin, DeleteView):
    """_summary_

    Args:
        SuccessMessageMixin (_type_): _description_
        LoginRequiredMixin (_type_): _description_
        generic (_type_): _description_

    Returns:
        _type_: _description_
    """
    model = BookReview
    success_url = reverse_lazy('admin_only')
    success_message = "Book Review successfully deleted!"
