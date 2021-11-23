from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from watchlist_app.api.serializers import WatchListSerializer, StreamPlatformSerializer
from core.models import WatchListModel, StreamPlatformModel


class StreamPlatformView(APIView):
    def get(self, request):
        stream_platform = StreamPlatformModel.objects.all()
        serializer = StreamPlatformSerializer(
            stream_platform,
            many=True
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = StreamPlatformSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer.save()
        return Response(serializer.data)


class WatchListView(APIView):

    def get(self, request):
        movies = WatchListModel.objects.all()
        serializer = WatchListSerializer(
            movies,
            many=True
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = WatchListSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer.save()
        return Response(serializer.data)


class WatchDetail(APIView):

    def get(self, request, pk):
        try:
            movie = WatchListModel.objects.get(pk=pk)
            serializer = WatchListSerializer(movie)
            return Response(serializer.data)
        except WatchListModel.DoesNotExist:
            return Response(
                {'error': 'Movie not found'},
                status=status.HTTP_404_NOT_FOUND
            )

    def put(self, request, pk):
        movie = WatchListModel.objects.get(pk=pk)
        serializer = WatchListSerializer(
            movie,
            data=request.data
        )
        if not serializer.is_valid():
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        movie = WatchListModel.objects.get(pk=pk)
        movie.delete()
        return Response(
            {'message': 'File deleted'},
            status=status.HTTP_204_NO_CONTENT
        )

# @api_view(['GET', 'POST'])
# def movie_list(request):
#     if request.method == 'GET':
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(
#             movies,
#             many=True
#         )
#         return Response(serializer.data)
#
#     if request.method == 'POST':
#         serializer = MovieSerializer(data=request.data)
#         if not serializer.is_valid():
#             return Response(
#                 serializer.errors,
#                 status=status.HTTP_400_BAD_REQUEST
#             )
#         serializer.save()
#         return Response(serializer.data)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def movie_details(request, pk):
#     if request.method == 'GET':
#         try:
#             movie = Movie.objects.get(pk=pk)
#             serializer = MovieSerializer(movie)
#             return Response(serializer.data)
#         except Movie.DoesNotExist:
#             return Response(
#                 {'error': 'Movie not found'},
#                 status=status.HTTP_404_NOT_FOUND
#             )
#
#     if request.method == 'PUT':
#         movie = Movie.objects.get(pk=pk)
#         serializer = MovieSerializer(
#             movie,
#             data=request.data
#         )
#         if not serializer.is_valid():
#             return Response(
#                 serializer.errors,
#                 status=status.HTTP_400_BAD_REQUEST
#             )
#
#         serializer.save()
#         return Response(serializer.data)
#
#     if request.method == 'DELETE':
#         movie = Movie.objects.get(pk=pk)
#         movie.delete()
#         return Response(
#             {'message': 'File deleted'},
#             status=status.HTTP_204_NO_CONTENT
#         )
