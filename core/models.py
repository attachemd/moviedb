from django.db import models


class WatchList(models.Model):
    title = models.CharField(max_length=30)
    about = models.CharField(max_length=150)
    website = models.URLField(max_length=100)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title