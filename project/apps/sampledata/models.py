from django.db import models
from django.contrib.auth.models import User
import datetime


class Book(models.Model):
    created = models.DateTimeField(auto_now_add=True, default=datetime.datetime.now)
    owner = models.ForeignKey('auth.User', related_name='books')
    title = models.CharField(max_length=100, default='Unknown Title')
    author = models.ForeignKey(User)
    year = models.SmallIntegerField(default=1900, max_length=4)
    isbn = models.CharField(max_length=13)
    summary = models.TextField(help_text='Description of this book', blank=True)

    class Meta:
        ordering = ('created',)

    def __unicode__(self):
        return self.title
