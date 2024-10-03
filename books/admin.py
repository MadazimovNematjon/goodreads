from django.contrib import admin
from users.models import CustomUser
from books.models import Book, Author, BookReview, BookAuthor


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'isbn',)
    search_fields = ('title', 'isbn')


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('email',)
    search_fields = ('email',)


class BookReviewAdmin(admin.ModelAdmin):
    list_display = ('author', 'book', 'review_text')
    search_fields = ('author', 'book',)


class BookAuthorAdmin(admin.ModelAdmin):
    list_display = ('author', 'book')
    search_fields = ('author', 'book')


# class UserAdmin(admin.ModelAdmin):
#     list_display = ('email', 'first_name', 'last_name')
#     search_fields = ('email', 'first_name', 'last_name')


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(BookReview, BookReviewAdmin)
admin.site.register(BookAuthor, BookAuthorAdmin)
# admin.site.register(User, UserAdmin)
