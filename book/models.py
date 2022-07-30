from unicodedata import category
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Genre(models.Model):
    """_summary_

    Args:
        models (_type_): _description_

    Returns:
        _type_: _description_
    """
    genre_name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=200, unique=True)
 
    def __str__(self):
        return self.genre_name

class Book(models.Model):
    """_summary_

    Args:
        models (_type_): _description_

    Returns:
        _type_: _description_
    """
    title = models.CharField(max_length=200, null=False, blank=False)
    book_author = models.CharField(max_length=200, null=False, blank=False)
    book_image = CloudinaryField('image', default='placeholder')
    book_blurb = models.TextField()
    book_genre = models.ForeignKey(Genre, on_delete=models.PROTECT, related_name='book_genre')
    slug = models.SlugField(max_length=200, unique=True)
    book_approved = models.BooleanField(default=False)
    book_created_on = models.DateTimeField(auto_now_add=True)
    book_favourites = models.ManyToManyField(
        User,
        related_name='book_favourites',
        blank=True)

    class Meta:
        """_summary_
        """
        ordering = ['-book_created_on']
        constraints = [
            models.UniqueConstraint(fields=['title', 'book_author'], name='unique_book_listing_ci')
        ]

    def __str__(self):
        return self.title

    
class BookReview(models.Model):
    """_summary_

    Args:
        models (_type_): _description_

    Returns:
        _type_: _description_
    """

    book_listing = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    review_username = models.ForeignKey(User, on_delete=models.CASCADE, related_name='review_author')
    review_detail = models.TextField()
    review_created_on = models.DateTimeField(auto_now_add=True)
    review_approved = models.BooleanField(default=False)
  
    class Meta:
        """_summary_
        """
        ordering = ['-review_created_on']

    def __str__(self):
        return f"Review {self.review_detail} by {self.review_username}"
  