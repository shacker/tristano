from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db.models import signals

from profiles.signals import create_profile


class Profile(models.Model):
    user = models.OneToOneField(User, unique=True)
    bio = models.TextField(help_text='A bit about yourself')
    influences = models.TextField(help_text='Musicians/artists who inspire you')
    social_avatar_url = models.URLField(default='/static/img/default-user-image.png')

    def set_social_avatar_url(self, request):
        '''
        To avoid a lot of calculation for every social avatar, store its calculated URL on the profile.
        Run this every time someone logs in with social so that remote avatar changes are reflected here.

        Normal login avatars use either uploaded image or via gravatar, but that's handled in pic_or_gravatar template tag.

        For sites that don't display long lists of user profiles with icons, could probably do without this function and just
        grab it directly from the social_account.extra_data directly.
        '''

        # Is this a social account?
        if self.user.socialaccount_set.all().count() > 0:
            sa = self.user.socialaccount_set.all()[0]

            if sa.provider == "twitter":
                # Hack: Twitter API returns the 48x48 version - we want want bigger.
                imgurl = sa.extra_data['profile_image_url_https'].replace('_normal', '_bigger')

            elif sa.provider == "google":
                imgurl = sa.extra_data['picture']

            elif sa.provider == "facebook":
                imgurl = "http://graph.facebook.com/{uid}/picture?type=large".format(uid=str(sa.uid))

            else:
                pass  # Other networks here...

            self.social_avatar_url = imgurl
            self.save()


    def display_name(self):
        # Separate from __unicode__ for use on public site
        if self.user.first_name and self.user.last_name:
            display_string = "{first} {last}".format(
                first=self.user.first_name,
                last=self.user.last_name)
        elif self.user.first_name and not self.user.last_name:
            display_string = "{first}".format(
                first=self.user.first_name)
        else:
            display_string = "{uname}".format(
                uname=self.user.username)

        return display_string

    def get_absolute_url(self):
        return reverse('profile_update')

    def __unicode__(self):

        display_string = "{display} ({uname})".format(display=self.display_name(), uname=self.user.username)
        return display_string


# When User instance is saved, trigger creation of corresponding profile.
# This covers instances of Users created from CLI or /admin, not just all-auth
signals.post_save.connect(create_profile, sender=User)


# When account is created via social, fire django-allauth signal to populate Django User record.
from allauth.account.signals import user_signed_up, user_logged_in
from django.dispatch import receiver

@receiver(user_signed_up)
def user_signed_up_(request, user, sociallogin=None, **kwargs):
    '''
    When a social account is created successfully and this signal is received,
    django-allauth passes in the sociallogin param, giving access to metadata on the remote account, e.g.:

    sociallogin.account.provider  # e.g. 'twitter'
    sociallogin.account.get_avatar_url()
    sociallogin.account.get_profile_url()
    sociallogin.account.extra_data['screen_name']

    See the socialaccount_socialaccount table for more in the 'extra_data' field.
    '''

    if sociallogin:
        # Extract first / last names from social nets and store on User record
        if sociallogin.account.provider == 'twitter':
            name = sociallogin.account.extra_data['name']
            user.first_name = name.split()[0]
            user.last_name = name.split()[1]

        if sociallogin.account.provider == 'facebook':
            user.first_name = sociallogin.account.extra_data['first_name']
            user.last_name = sociallogin.account.extra_data['last_name']

        if sociallogin.account.provider == 'google':
            user.first_name = sociallogin.account.extra_data['given_name']
            user.last_name = sociallogin.account.extra_data['family_name']

        user.save()


@receiver(user_logged_in)
def user_logged_in_(request, user, sociallogin=None, **kwargs):
    '''
    On successful social login (not signup), refresh profile details etc.
    For new users, create profile first!
    '''

    p, created = Profile.objects.get_or_create(user=user)   # 'created' will be true or false
    p.set_social_avatar_url(p)
