from django.test import TestCase
from django.contrib.auth.models import User
from profiles.models import Profile


class ProfileTest(TestCase):

    def setUp(self):
        self.newuser = User.objects.create_user('zjzjzj', 'zj@example.com', 'somepass')
        self.newuser.first_name = "ZJ"
        self.newuser.last_name = "Smith"
        self.newuser.save()


    def test_new_user_gets_profile(self):
        """
        Ensures that newly created User objects always get matching Profile objects
        """

        # A bit odd, but newuser object should be identical to user object belonging
        # to the profile that belongs to newuser
        self.assertEqual(self.newuser.profile.user, self.newuser)


    def test_display_name(self):
        """
        display_name() method on Profile should assemble first and last names
        """

        profile = self.newuser.profile
        self.assertEqual(profile.display_name(), "ZJ Smith")
