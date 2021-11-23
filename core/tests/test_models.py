from django.test import TestCase

from django.contrib.auth import get_user_model
from faker import Faker

from watchlist_app.tests.factories import WatchListFactory

faker = Faker()


class ModelTests(TestCase):

    def test_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            username=faker.user_name(),
            email=faker.email(),
            password='pass'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_watchlist_str(self):
        """Test the movie string representation"""
        watch_list = WatchListFactory()
        self.assertEqual(str(watch_list), watch_list.title)
