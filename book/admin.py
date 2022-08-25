from django.contrib import admin
from .models import Book, BookReview, Genre


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """
    Add fields for admin panel for the Book Model
    Set the prepopulated fields of slug with the
    title and book_author fields
    """
    prepopulated_fields = {'slug': ('title', 'book_author')}
    list_filter = ('book_approved', 'book_created_on')
    list_display = ('title', 'book_author', 'slug', 'book_genre',
                    'book_created_on', 'book_approved')
    search_fields = ('title', 'book_author')
    actions = ['approve_books']

    def approve_books(self, request, queryset):
        """
        Update the book_approve field
        """
        queryset.update(book_approved=True)


@admin.register(BookReview)
class BookReviewAdmin(admin.ModelAdmin):
    """
    Add the fields for the Admin Panel for the BookReview Model
    """

    list_filter = ('review_approved', 'review_created_on')
    list_display = ('review_username', 'review_detail', 'book_listing',
                    'review_created_on', 'review_approved')
    search_fields = ('review_username', 'review_detail')
    actions = ['approve_reviews']

    def approve_reviews(self, request, queryset):
        """
        Update the review_approve field
        """
        queryset.update(review_approved=True)


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    """
    Add the fields for the Admin Panel for the Genre Model
    Set the prepopulated fields of slug with the
    genre_name fields
    """

    prepopulated_fields = {'slug': ['genre_name']}
    list_filter = ['genre_name']
    list_display = ('genre_name', 'genre_image', 'slug')
