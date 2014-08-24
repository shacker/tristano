from django.views.generic import TemplateView


class BooksView(TemplateView):
    """
    Stub list view for user's books; hand off to Angular for data display.
    """

    template_name = "books/books.html"


