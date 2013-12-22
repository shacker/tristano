from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length=100, default='Unknown Title')
    author = models.OneToOneField(User, unique=True)
    year = models.SmallIntegerField(default=1900, max_length=4)
    isbn = models.CharField(max_length=13)
    summary = models.TextField(help_text='Description of this book', blank=True)

    def __unicode__(self):
        return self.title
