from rest_framework import serializers
from sampledata.models import Book
from django.contrib.auth.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(view_name='snippet-detail', many=True)

    class Meta:
        model = User
        fields = ('url', 'username', 'email')



class BookSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.Field(source='owner.username')
    # highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

    class Meta:
        model = Book
        fields = ('url', 'title', 'author', 'year', 'isbn', 'summary')


