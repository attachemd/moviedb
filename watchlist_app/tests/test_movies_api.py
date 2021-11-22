from unittest import TestCase

from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

from core.models import Movie
from watchlist_app.api.serializers import MovieSerializer

MOVIES_URL = reverse('movie_list')


class MoviesApiTests(TestCase):
    """Test the authorized user tags API"""

    def setUp(self):
        self.client = APIClient()

    def test_retrieve_movies(self):
        """Test retrieving tags"""
        Movie.objects.create(
            name='Mayer, Steele and Frederick',
            about='Memory produce keep score memory.',
            website='https://marshall.com/',
            active=True,
        )
        Movie.objects.create(
            name='King, Hudson and Marshall',
            about='Really which animal other plant relationship.',
            website='https://tucker-hamilton.info/',
            active=False,
        )

        res = self.client.get(MOVIES_URL)

        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_create_movie_successful(self):
        """Test creating a new tag"""
        payload = {
            'name': 'Mendez LLC',
            'about': 'Room fill government.',
            'website': 'https://dunn.com/',
            'active': True,
        }
        self.client.post(MOVIES_URL, payload)

        exists = Movie.objects.filter(
            name=payload['name'],
            about=payload['about'],
            website=payload['website'],
            active=payload['active'],
        ).exists()
        self.assertTrue(exists)

    def test_create_movie_invalid(self):
        """Test creating a new tag with invalid payload"""
        payload = {
            'name': '',
        }
        res = self.client.post(MOVIES_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_valid_update_movie(self):
        """
        Validated data case
        """
        movie = Movie.objects.create(
            name='King, Hudson and Marshall',
            about='Really which animal other plant relationship.',
            website='https://tucker-hamilton.info/',
            active=False,
        )
        new_data = {
            'name': 'Mendez LLC',
            'about': 'Room fill government.',
            'website': 'https://dunn.com/',
            'active': True,
        }
        response = self.client.put(
            reverse('movie_detail', kwargs={'pk': movie.pk}),
            data=new_data
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_update_movie(self):
        """
        Invalid data case
        """
        movie = Movie.objects.create(
            name='King, Hudson and Marshall',
            about='Really which animal other plant relationship.',
            website='https://tucker-hamilton.info/',
            active=False,
        )
        new_data = {
            'name': '',
            'about': 'Room fill government.',
            'website': 'https://dunn.com/',
            'active': True,
        }
        response = self.client.put(
            reverse('movie_detail', kwargs={'pk': movie.pk}),
            data=new_data
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_movie(self):
        movie = Movie.objects.create(
            name='King, Hudson and Marshall',
            about='Really which animal other plant relationship.',
            website='https://tucker-hamilton.info/',
            active=False,
        )
        url = reverse('movie_detail', kwargs={'pk': movie.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
