from django.http import JsonResponse

from core.models import Movie


def movie_list(request):
    movies = Movie.objects.all()
    data = {
        'movies': list(movies.values())
    }
    return JsonResponse(data)


def movie_details(request, pk):
    movie = Movie.objects.get(pk=pk)
    data = {
        'name': movie.name,
        'about': movie.about,
        'website': movie.website
    }
    return JsonResponse(data)
