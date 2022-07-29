from django.contrib import admin
from .models import Book, BookReview, Genre

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):

    prepopulated_fields = {'slug': ('title', 'book_author')}
    list_filter = ('book_approved', 'book_created_on')
    list_display = ('title', 'book_author', 'slug', 'book_created_on', 'book_approved' )
    search_fields = ('title', 'book_author')
    actions = ['approve_books']

    def approve_books(self, request, queryset):
        queryset.update(book_approved=True)


@admin.register(BookReview)
class BookReviewAdmin(admin.ModelAdmin):

    list_filter = ('review_approved', 'review_created_on')
    list_display = ('review_username', 'review_detail', 'book_listing','review_created_on', 'review_approved' )
    search_fields = ('review_username', 'review_detail')
    actions = ['approve_reviews']

    def approve_reviews(self, request, queryset):
        queryset.update(review_approved=True)


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):

    prepopulated_fields = {'slug': ['genre_name']}
    list_filter = ['genre_name']
    list_display = ['genre_name']
