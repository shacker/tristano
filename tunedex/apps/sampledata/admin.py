from django.contrib import admin
from sampledata.models import Book

class BookAdmin(admin.ModelAdmin):
	list_display = ('title', 'author', 'year')

admin.site.register(Book, BookAdmin)