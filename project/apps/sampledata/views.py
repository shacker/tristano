from django.views.generic import TemplateView


class BooksListView(TemplateView):
    """
    Stub list view for user's books; hand off to Angular for data display.
    """

    template_name = "books/list.html"
