from django.db import models


class StreamPlatformModel(models.Model):
    name = models.CharField(max_length=30)
    about = models.CharField(max_length=150)
    website = models.URLField(max_length=100)

    def __str__(self):
        return self.name


class WatchListModel(models.Model):
    title = models.CharField(max_length=30)
    platform = models.ForeignKey(
        StreamPlatformModel,
        on_delete=models.CASCADE,
        related_name='watchlist'
    )
    storyline = models.CharField(max_length=150)
    website = models.URLField(max_length=100)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
