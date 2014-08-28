from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView

from sampledata.models import Book



class BooksListView(TemplateView):
    """
    Stub list view for user's books; hand off to Angular for data display.
    """

    template_name = "books/list.html"


class BooksStaticListView(ListView):
    '''
    Example of class-based list view for static display
    '''
    model = Book
    template_name = "books/list_static.html"


class BooksStaticDetailView(DetailView):
    '''
    Example of class-based detail view for static display
    '''
    model = Book
    template_name = "books/detail_static.html"
