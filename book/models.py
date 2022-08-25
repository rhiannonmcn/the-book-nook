from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Genre(models.Model):
    """
    Model for Book Genres
    """
    genre_name = models.CharField(max_length=50)
    genre_image = CloudinaryField('image', default='placeholder')
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.genre_name


class Book(models.Model):
    """
    Model for a Book
    """
    title = models.CharField(max_length=200, null=False, blank=False)
    book_author = models.CharField(max_length=200, null=False, blank=False)
    book_image = CloudinaryField('image', default='placeholder')
    book_blurb = models.TextField()
    book_genre = models.ForeignKey(Genre, on_delete=models.PROTECT,
                                   related_name='book_genre')
    slug = models.SlugField(max_length=200, unique=True)
    book_approved = models.BooleanField(default=False)
    book_created_on = models.DateTimeField(auto_now_add=True)
    book_favourites = models.ManyToManyField(
        User,
        related_name='book_favourites',
        blank=True)

    class Meta:
        """
        books are ordered from the newest to the oldest
        sets the unique constraints
        """
        ordering = ['-book_created_on']
        constraints = [
            models.UniqueConstraint(fields=['title', 'book_author'],
                                    name='unique_book_listing_ci')
        ]

    def __str__(self):
        return self.title

    def number_of_favourites(self):
        """
        Returns total number of times users have bookmarked a book
        """
        return self.book_favourites.count()


class BookReview(models.Model):
    """
    Model for review
    """

    book_listing = models.ForeignKey(Book, on_delete=models.CASCADE,
                                     related_name='reviews')
    review_username = models.ForeignKey(User, on_delete=models.CASCADE,
                                        related_name='review_author')
    review_detail = models.TextField()
    review_created_on = models.DateTimeField(auto_now_add=True)
    review_approved = models.BooleanField(default=False)

    class Meta:
        """
        reviews ordered from newest to oldest
        """
        ordering = ['-review_created_on']

    def __str__(self):
        return f"Review {self.review_detail} by {self.review_username}"
