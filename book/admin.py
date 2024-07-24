from django.contrib import admin
from book.models import Author, Book

# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    list_display=["name"]
admin.site.register(Author, AuthorAdmin)

class BookAdmin(admin.ModelAdmin):
    list_display = ["title", "author_id", "price"]
admin.site.register(Book, BookAdmin)