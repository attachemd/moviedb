from django.http import JsonResponse

from watchlist_app.models import Movie


def movie_list(request):
    movies = Movie.objects.all()
    data = {
        'movies': list(movies.values())
    }
    return JsonResponse(data)
