from rest_framework import serializers 
from .models import Book, Exchange, City, Genre

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id','title','author','owner','book_status']

class ExchangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exchange
        fields = ['id','book','getter']

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['id','name']

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id','name']