from .models import BookReview, Book
from django import forms



class BookForm(forms.ModelForm):
    class Meta:
        model = BookReview
        fields  = ('review_detail',)
        
        custom_names = {'email': 'email_address'}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['review_detail'].label = 'Review'
        
        
class AddBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'book_author', 'book_image','book_blurb', 'book_genre')
    
    