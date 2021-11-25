from django.urls import path, include
from rest_framework.routers import DefaultRouter

from watchlist_app.api import views
from watchlist_app.api.views import StreamPlatformView

router = DefaultRouter()
router.register('stream', StreamPlatformView, basename='stream_platform')

urlpatterns = [
    # path('list/', views.movie_list, name='movie_list'),
    # path('<int:pk>', views.movie_details, name='movie_detail'),
    path('list/', views.WatchListView.as_view(), name='movie_list'),
    path('list/<int:pk>', views.WatchDetail.as_view(), name='movie_detail'),

    path('', include(router.urls)),
    # path('stream/', views.StreamPlatformView.as_view(), name='stream'),
    # path('stream/<int:pk>', views.StreamPlatformDetailView.as_view(), name='stream_detail'),

    # path('review/', views.ReviewView.as_view(), name='review_list'),
    # path('review/<int:pk>', views.ReviewDetailView.as_view(), name='review_detail'),
    path('stream/<int:pk>/review/', views.ReviewView.as_view(), name='review_list'),
    path('stream/<int:pk>/review-create/', views.ReviewCreateView.as_view(), name='review_create'),
    path('stream/review/<int:pk>', views.ReviewDetailView.as_view(), name='review_detail'),
]
