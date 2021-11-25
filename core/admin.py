from django.contrib import admin

from core.models import WatchListModel, StreamPlatformModel, ReviewModel

admin.site.register(WatchListModel)
admin.site.register(StreamPlatformModel)
admin.site.register(ReviewModel)
