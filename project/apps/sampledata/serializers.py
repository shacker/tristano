from rest_framework import serializers
from sampledata.models import Book
from django.contrib.auth.models import User


class BookSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.Field(source='owner.username')

    class Meta:
        model = Book
        fields = ('url', 'title', 'author', 'year', 'isbn', 'summary')
