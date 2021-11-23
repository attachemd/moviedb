from unittest import TestCase
from datetime import datetime

import django
from django.urls import reverse
from django.utils import timezone
from faker import Faker
from rest_framework.test import APIClient
from rest_framework import status

from core.models import WatchListModel
from watchlist_app.api.serializers import WatchListSerializer
from watchlist_app.tests.factories import WatchListFactory, StreamPlatformFactory

MOVIES_URL = reverse('movie_list')


def movie_url_pk(pk):
    return reverse('movie_detail', kwargs={'pk': pk})


def sample_stream_platform(user, name='Main course'):
    return StreamPlatformFactory()


def valid_watch_list(stream_platform_id):
    return {
        'title': faker.company(),
        'platform': stream_platform_id,
        'storyline': faker.sentence(),
        'website': faker.url(),
        'active': faker.boolean(),
        # 'created': datetime.now().strftime("%A, %d. %B %Y %I:%M%p")
        # 'created': str(timezone.now())
        # 'created': datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%fZ")
        # 'created': datetime.now().strftime("%Y-%m-%d %H:%M[:%S[.uuuuuu]][TZ]")
        # 'created': datetime.now().strftime("YYYY-MM-DD HH:MM[:ss[.uuuuuu]][TZ]")
    }


faker = Faker()


class MoviesApiTests(TestCase):
    """Test the authorized user tags API"""

    def setUp(self):
        self.client = APIClient()
        self.stream_platform = StreamPlatformFactory()
        self.valid_watch_list = valid_watch_list(self.stream_platform.id)

        self.invalid_watch_list = {
            'title': '',
        }

    def test_retrieve_movies(self):
        """Test retrieving tags"""
        WatchListFactory(platform=self.stream_platform)
        WatchListFactory(platform=self.stream_platform)

        res = self.client.get(MOVIES_URL)

        movies = WatchListModel.objects.all()
        serializer = WatchListSerializer(movies, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_create_movie_successful(self):
        """Test creating a new tag"""

        res = self.client.post(MOVIES_URL, self.valid_watch_list)
        print("res: ")
        print(res)
        # exists = WatchList.objects.filter(
        #     title=self.valid_watch_list['title'],
        #     about=self.valid_watch_list['about'],
        #     website=self.valid_watch_list['website'],
        #     active=self.valid_watch_list['active'],
        # ).exists()

        exists = WatchListModel.objects.filter(
            **self.valid_watch_list
        ).exists()
        self.assertTrue(exists)

    def test_create_movie_invalid(self):
        """Test creating a new tag with invalid payload"""
        res = self.client.post(MOVIES_URL, self.invalid_watch_list)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_valid_update_movie(self):
        """
        Validated data case
        """
        movie = WatchListFactory(platform=self.stream_platform)
        response = self.client.put(
            movie_url_pk(movie.pk),
            data=self.valid_watch_list
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_update_movie(self):
        """
        Invalid data case
        """
        movie = WatchListFactory(platform=self.stream_platform)
        response = self.client.put(
            movie_url_pk(movie.pk),
            data=self.invalid_watch_list
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_movie(self):
        movie = WatchListFactory(platform=self.stream_platform)
        response = self.client.delete(movie_url_pk(movie.pk))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
