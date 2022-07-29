from .models import BookReview
from django import forms


class BookForm(forms.ModelForm):
    class Meta:
        model = BookReview
        fields  = ('review_detail',)