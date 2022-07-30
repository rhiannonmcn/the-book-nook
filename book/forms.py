from .models import BookReview
from django import forms


class BookForm(forms.ModelForm):
    class Meta:
        model = BookReview
        fields  = ('review_detail',)
        
        custom_names = {'email': 'email_address'}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['review_detail'].label = 'Review'