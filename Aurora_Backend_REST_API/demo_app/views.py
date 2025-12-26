# from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Item, Book, Author
from .serializers import ItemSerializer, BookSerializer, AuthorSerializer

from rest_framework.views import APIView
from rest_framework.response import Response

"""This automatically provides:
-Create
-Read (list & detail)-
-Update
-Delete"""
class ItemViewSet(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class AuthorList(APIView):
    def get(self, request):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)

class BookList(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
    
