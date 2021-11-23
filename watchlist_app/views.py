from django.http import JsonResponse

from core.models import WatchListModel


def movie_list(request):
    movies = WatchListModel.objects.all()
    data = {
        'movies': list(movies.values())
    }
    return JsonResponse(data)


def movie_details(request, pk):
    movie = WatchListModel.objects.get(pk=pk)
    data = {
        'title': movie.title,
        'about': movie.about,
        'website': movie.website
    }
    return JsonResponse(data)
