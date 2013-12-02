from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.ForeignKey(User, unique=True)
    bio = models.TextField(help_text='A bit about yourself')
    influences = models.TextField(help_text='Musicians/artists who inspire you')
    avatar = models.ImageField(upload_to='profiles', blank=True, null=True)

    def __unicode__(self):
        if self.user.first_name and self.user.last_name:
            return u'%s %s' % (self.user.first_name, self.user.last_name)
        elif self.user.first_name:
            return u'%s' % (self.user.first_name)        
        else:
            return self.user.username
