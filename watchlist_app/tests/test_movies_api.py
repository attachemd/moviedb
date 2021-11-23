from unittest import TestCase
from datetime import datetime

import django
from django.urls import reverse
from django.utils import timezone
from faker import Faker
from rest_framework.test import APIClient
from rest_framework import status

from core.models import WatchList
from watchlist_app.api.serializers import MovieSerializer
from watchlist_app.tests.factories import WatchListFactory

MOVIES_URL = reverse('movie_list')


def movie_url_pk(pk):
    return reverse('movie_detail', kwargs={'pk': pk})


faker = Faker()


VALID_WATCH_LIST = {
    'title': faker.company(),
    'about': faker.sentence(),
    'website': faker.url(),
    'active': faker.boolean(),
    # 'created': datetime.now().strftime("%A, %d. %B %Y %I:%M%p")
    # 'created': str(timezone.now())
    # 'created': datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%fZ")
    # 'created': datetime.now().strftime("%Y-%m-%d %H:%M[:%S[.uuuuuu]][TZ]")
    # 'created': datetime.now().strftime("YYYY-MM-DD HH:MM[:ss[.uuuuuu]][TZ]")
}

print("VALID_WATCH_LIST: ")
print(VALID_WATCH_LIST)

INVALID_WATCH_LIST = {
    'title': '',
}


class MoviesApiTests(TestCase):
    """Test the authorized user tags API"""

    def setUp(self):
        self.client = APIClient()

    def test_retrieve_movies(self):
        """Test retrieving tags"""
        WatchListFactory()
        WatchListFactory()

        res = self.client.get(MOVIES_URL)

        movies = WatchList.objects.all()
        serializer = MovieSerializer(movies, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_create_movie_successful(self):
        """Test creating a new tag"""

        res = self.client.post(MOVIES_URL, VALID_WATCH_LIST)

        # exists = WatchList.objects.filter(
        #     title=VALID_WATCH_LIST['title'],
        #     about=VALID_WATCH_LIST['about'],
        #     website=VALID_WATCH_LIST['website'],
        #     active=VALID_WATCH_LIST['active'],
        # ).exists()
        temp = WatchList.objects.filter(
            **VALID_WATCH_LIST
        )
        print('res.data: ')
        print(res.data)
        print('VALID_WATCH_LIST after: ')
        print(VALID_WATCH_LIST)
        exists = WatchList.objects.filter(
            **VALID_WATCH_LIST
        ).exists()
        print('VALID_WATCH_LIST before: ')
        print(VALID_WATCH_LIST)
        self.assertTrue(exists)

    def test_create_movie_invalid(self):
        """Test creating a new tag with invalid payload"""
        res = self.client.post(MOVIES_URL, INVALID_WATCH_LIST)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_valid_update_movie(self):
        """
        Validated data case
        """
        movie = WatchListFactory()
        response = self.client.put(
            movie_url_pk(movie.pk),
            data=VALID_WATCH_LIST
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_update_movie(self):
        """
        Invalid data case
        """
        movie = WatchListFactory()
        response = self.client.put(
            movie_url_pk(movie.pk),
            data=INVALID_WATCH_LIST
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_movie(self):
        movie = WatchListFactory()
        response = self.client.delete(movie_url_pk(movie.pk))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
