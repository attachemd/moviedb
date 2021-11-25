from django.shortcuts import get_object_or_404
from rest_framework import status, generics, mixins, viewsets
from rest_framework.decorators import api_view
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView

from watchlist_app.api.serializers import (
    WatchListSerializer,
    StreamPlatformSerializer,
    ReviewSerializer
)
from core.models import WatchListModel, StreamPlatformModel, ReviewModel


class ReviewCreateView(
    generics.CreateAPIView
):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return ReviewModel.objects.all()

    def perform_create(self, serializer):
        pk = self.kwargs['pk']
        watchlist = WatchListModel.objects.get(pk=pk)
        user = self.request.user
        review_queryset = ReviewModel.objects.filter(watchlist=watchlist, user=user)

        if review_queryset.exists():
            raise ValidationError('you are already reviewed this movie.')
        print("user: ")
        print(user)
        serializer.save(watchlist=watchlist, user=user)


class ReviewView(
    generics.ListAPIView
):
    # queryset = ReviewModel.objects.all()
    serializer_class = ReviewSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return ReviewModel.objects.filter(watchlist=pk)


class ReviewDetailView(
    generics.RetrieveUpdateDestroyAPIView
):
    queryset = ReviewModel.objects.all()
    serializer_class = ReviewSerializer


# class ReviewDetailView(
#     mixins.RetrieveModelMixin,
#     generics.GenericAPIView
# ):
#     queryset = ReviewModel.objects.all()
#     serializer_class = ReviewSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)


# class ReviewView(
#     mixins.ListModelMixin,
#     mixins.CreateModelMixin,
#     generics.GenericAPIView
# ):
#     queryset = ReviewModel.objects.all()
#     serializer_class = ReviewSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

class StreamPlatformView(viewsets.ModelViewSet):
    queryset = StreamPlatformModel.objects.all()
    serializer_class = StreamPlatformSerializer


# class StreamPlatformView(viewsets.ViewSet):
#
#     def list(self, request):
#         queryset = StreamPlatformModel.objects.all()
#         serializer = StreamPlatformSerializer(queryset, many=True)
#         return Response(serializer.data)
#
#     def retrieve(self, request, pk=None):
#         queryset = StreamPlatformModel.objects.all()
#         watchlist = get_object_or_404(queryset, pk=pk)
#         serializer = StreamPlatformSerializer(watchlist)
#         return Response(serializer.data)
#
#     def create(self, request):
#         serializer = StreamPlatformSerializer(data=request.data)
#         if not serializer.is_valid():
#             return Response(serializer.errors)
#         serializer.save()
#         return Response(serializer.data)


# class StreamPlatformView(APIView):
#     def get(self, request):
#         stream_platform = StreamPlatformModel.objects.all()
#         serializer = StreamPlatformSerializer(
#             stream_platform,
#             many=True
#         )
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = StreamPlatformSerializer(data=request.data)
#         if not serializer.is_valid():
#             return Response(
#                 serializer.errors,
#                 status=status.HTTP_400_BAD_REQUEST
#             )
#         serializer.save()
#         return Response(serializer.data)
#
#
# class StreamPlatformDetailView(APIView):
#     def get(self, request, pk):
#         try:
#             stream_platform = StreamPlatformModel.objects.get(pk=pk)
#             serializer = StreamPlatformSerializer(stream_platform)
#             return Response(serializer.data)
#         except StreamPlatformModel.DoesNotExist:
#             return Response(
#                 {'error': 'Movie not found'},
#                 status=status.HTTP_404_NOT_FOUND
#             )
#
#     def put(self, request, pk):
#         stream_platform = StreamPlatformModel.objects.get(pk=pk)
#         serializer = StreamPlatformSerializer(
#             stream_platform,
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
#     def delete(self, request, pk):
#         stream_platform = StreamPlatformModel.objects.get(pk=pk)
#         stream_platform.delete()
#         return Response(
#             {'message': 'File deleted'},
#             status=status.HTTP_204_NO_CONTENT
#         )


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
