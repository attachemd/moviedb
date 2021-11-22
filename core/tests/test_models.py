from django.test import TestCase

from django.contrib.auth import get_user_model

from core import models


class ModelTests(TestCase):

    def test_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            username='superuser',
            email='superuser@email.com',
            password='pass'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_tag_str(self):
        """Test the movie string representation"""
        movie = models.Movie.objects.create(
            name='Mayer, Steele and Frederick',
            about='Memory produce keep score memory.',
            website='https://marshall.com/',
        )
        self.assertEqual(str(movie), movie.name)
