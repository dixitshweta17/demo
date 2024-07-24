
from django.urls import path
from book.models import Book
from book.views import BookView

urlpatterns = [

    path("book/", BookView.as_view(), name="book"),
    path("book/<int:id>", BookView.as_view(), name="book_detail")
]