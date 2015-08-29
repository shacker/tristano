from rest_framework import serializers
from sampledata.models import Book
from django.contrib.auth.models import User


class BookSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.Field(source='owner.username')

    def to_internal_value(self, data):
        value = super(UppercaseCharField, self).to_internal_value(data)
        if value != value.upper():
            raise serializers.ValidationError('The input should be uppercase only.')
        return value

    class Meta:
        model = Book
        fields = ('id', 'url', 'title', 'author', 'year', 'isbn', 'summary', 'owner')
