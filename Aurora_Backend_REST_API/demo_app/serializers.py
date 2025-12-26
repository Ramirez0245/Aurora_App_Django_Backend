from rest_framework import serializers
from .models import Item, Book, Author

from django.conf import settings


# Serializers convert model instances ↔ JSON.
class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'




class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()  # nested serializer

    class Meta:
        model = Book
        fields = '__all__'
        print("START: BookSerializer initialized")
        print(settings.DATABASES['default']['ENGINE'])    