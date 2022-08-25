from .models import BookReview, Book
from django import forms


class BookForm(forms.ModelForm):
    """
    Form for Book Review
    """
    class Meta:
        """
        Form has field of review_detail
        from BookReview model
        It has a custom name of Review
        """
        model = BookReview
        fields = ('review_detail',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['review_detail'].label = 'Review'


class AddBookForm(forms.ModelForm):
    """_summary_
    Form for Adding a Book
    """
    class Meta:
        """
        Form has the title, book_author, book_image,
        book_blurb and book_genre fields from the
        Book model
        """
        model = Book
        fields = ('title', 'book_author', 'book_image',
                  'book_blurb', 'book_genre')
