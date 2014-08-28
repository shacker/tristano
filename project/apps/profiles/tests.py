from django.test import TestCase
from django.contrib.auth.models import User
from profiles.models import Profile


class ProfileTest(TestCase):
    fixtures = ['test_users.json']

    def setUp(self):
        self.newuser = User.objects.create_user('zjzjzj', 'zj@example.com', 'somepass')
        self.newuser.first_name = "ZJ"
        self.newuser.last_name = "Smith"
        self.newuser.save()


    def test_fixture_loaded(self):
        # Make sure we can retrieve a known test user from the fixture data
        self.assertTrue(User.objects.get(username='mary'))


    def test_new_user_gets_profile(self):
        """
        Ensures that newly created User objects always get matching Profile objects
        """

        # Verify that a related profile object now exists
        self.assertTrue(self.newuser.profile)


    def test_display_name(self):
        """
        display_name() method on Profile should assemble first and last names correctly.
        """

        profile = self.newuser.profile
        self.assertEqual(profile.display_name(), "ZJ Smith")
