from django.http import JsonResponse

from core.models import WatchList


def movie_list(request):
    movies = WatchList.objects.all()
    data = {
        'movies': list(movies.values())
    }
    return JsonResponse(data)


def movie_details(request, pk):
    movie = WatchList.objects.get(pk=pk)
    data = {
        'title': movie.title,
        'about': movie.about,
        'website': movie.website
    }
    return JsonResponse(data)
