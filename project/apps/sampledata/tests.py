from django.test import TestCase
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from sampledata.models import Book

class BookTest(TestCase):

    fixtures = ['test_users.json', 'test_books.json']


    def setUp(self):
        # Create an owner and an author to test Book record creation
        self.owner = User.objects.create_user('bob', 'bob@example.com', 'somepass')
        self.author = User.objects.create_user('maryjane', 'maryjane@example.com', 'somepass')

        self.book1 = Book.objects.create(
            owner = self.owner,
            author = self.author,
            title = "This is a test title",
            year = 1975
        )


    def test_fixture_loaded(self):
        # Make sure we can retrieve a known test book from the fixture data
        self.assertTrue(Book.objects.get(isbn='1923389845398'))


    def test_book1_saved(self):
        """
        Basic ability to save a book (in setUp) and retrieve it
        """
        self.book1.save()

        book = Book.objects.get(id=1)
        self.assertEqual(book.id, 1)


    def test_generic_list_view(self):
        """
        Generic CBV retrieval, named URL
        """

        response = self.client.get(reverse('books_list_static'))

        self.assertEqual(response.status_code, 200)


    def test_generic_detail_view(self):
        """
        Generic CBV retrieval of the first found book.
        """

        books = Book.objects.all()
        book_id = books[0].id  # Can't assume test book has ID 1, so get first book in db

        url = reverse('books_detail_static', kwargs={'pk': book_id})
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
