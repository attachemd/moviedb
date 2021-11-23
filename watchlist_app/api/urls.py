from django.urls import path

from watchlist_app.api import views

urlpatterns = [
    # path('list/', views.movie_list, name='movie_list'),
    # path('<int:pk>', views.movie_details, name='movie_detail'),
    path('list/', views.WatchListView.as_view(), name='movie_list'),
    path('<int:pk>', views.WatchDetail.as_view(), name='movie_detail'),
    path('stream/', views.StreamPlatformView.as_view(), name='stream'),
]
