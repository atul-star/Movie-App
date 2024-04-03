from django.db import models

# Create your models here.
from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100)
    poster = models.ImageField(upload_to='posters/')
    genres = models.CharField(max_length=200)
    rating = models.CharField(max_length=10)
    year_release = models.IntegerField()
    metacritic_rating = models.IntegerField()
    runtime = models.CharField(max_length=20)

    def __str__(self):
        return self.title
