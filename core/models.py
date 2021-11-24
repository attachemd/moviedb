from django.core.validators import MinValueValidator, MaxValueValidator
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


class ReviewModel(models.Model):
    watchlist = models.ForeignKey(
        WatchListModel,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    description = models.CharField(max_length=200, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.rating) + ' - ' + self.watchlist.title
