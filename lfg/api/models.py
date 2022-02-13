from django.db import models
from django.utils import timezone

class Videogame(models.model):
    name = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    release_date = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.name

# Create your models here.
