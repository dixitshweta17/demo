from rest_framework import serializers
from book.models import Book,Author

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model= Author
        fields = "__all__"


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model= Book
        fields = "__all__"

