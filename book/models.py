from unicodedata import category
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Category(models.Model):
    category = models.CharField(max_length=50) 
 
    def __str__(self):
        return self.category

class Book(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False)
    book_author = models.CharField(max_length=200, null=False, blank=False)
    book_image = CloudinaryField('image', default='placeholder')
    book_blurb = models.TextField()
    book_category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='book_category')
    slug = models.SlugField(max_length=200, unique=True)
    book_approved = models.BooleanField(default=False)
    book_created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-book_created_on']
        constraints = [
            models.UniqueConstraint(fields=['title', 'book_author'], name='unique_book_listing_ci')
        ]

    def __str__(self):
        return self.title

    
class BookReview(models.Model):
    book_listing = models.ForeignKey(Book, on_delete=models.PROTECT, related_name='reviews')
    review_username = models.ForeignKey(User, on_delete=models.CASCADE, related_name='review_author')
    review_detail = models.TextField()
    review_created_on = models.DateTimeField(auto_now_add=True)
    review_approved = models.BooleanField(default=False)
  
    class Meta:
        ordering = ['-review_created_on']

    def __str__(self):
        return self.id
  