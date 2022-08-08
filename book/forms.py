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
    


class ContactForm(forms.Form):
    """_summary_

    Args:
        forms (_type_): _description_
    """
    
    first_name = forms.CharField(label='First Name', max_length = 50, required=True)
    last_name = forms.CharField(label='Last Name', max_length = 50, required=True)
    email_address = forms.EmailField(label='Email', max_length = 150, required=True)
    message = forms.CharField(widget=forms.Textarea, label='Message', max_length = 2000, required=True)   