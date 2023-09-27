from rest_framework import serializers
from .models import authorModel, bookModel


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model=authorModel
        fields=('__all__')

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=bookModel
        fields=('__all__')