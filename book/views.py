from django.http import JsonResponse
from django.shortcuts import render
from book.models import Author, Book
from django.views import View
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView

from book.serializers import BookSerializer

# get, post, put and delete

# Create your views here.

class BookView(APIView):
    def get(self, request, format=None):
        queryset = Book.objects.all()
        serializer = BookSerializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    def post(self, request, format=None):

        title = request.data.get('title')
        author_id = request.data.get('author_id')
        price = request.data.get('price')

        author_id = Author.objects.get(id=author_id)
        
        queryset = Book.objects.create(title = title, author_id= author_id, price= price )
        serializer = BookSerializer(queryset)
        return JsonResponse (serializer.data)
    
    def put(self, request, *args, **kwargs):
        id = kwargs.get('id')
        title = request.data.get('title')
        author_id = request.data.get('author_id')
        price = request.data.get('price')

        try:
            book_instance = Book.objects.get(id=id)
        except Book.DoesNotExist:
            return JsonResponse({'error': 'Book not found'}, status=404)

        try:
            author = Author.objects.get(id=author_id)
        except Author.DoesNotExist:
            return JsonResponse({'error': 'Author not found'}, status=404)

        book_instance.title = title
        book_instance.author_id = author
        book_instance.price = price
        book_instance.save()
        
        serializer = BookSerializer(book_instance)
        
        return JsonResponse(serializer.data)
    
    def delete(self, request, *args, **kwargs):
        id = kwargs.get('id')

        try:
            book_instance = Book.objects.get(id=id)
        except Book.DoesNotExist:
            return JsonResponse({'error': 'Book not found'}, status=404)

        book_instance.delete()
        
        return JsonResponse({'message': 'Book deleted successfully'}, status=204)