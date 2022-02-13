from django.db import models
from django.utils import timezone
from django.conf import settings

class Videogame(models.model):
    name = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    release_date = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.name

class Party(models.model):
    name = models.CharField(max_length=200)
    videogame = models.ForeignKey(Videogame,on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.name

class Profile(models.model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    twitter = models.CharField(max_length=200)
    instagram = models.CharField(max_length=200)
    telegram = models.CharField(max_length=200)
    website = models.CharField(max_length=200)
    twitch = models.CharField(max_length=200)
    epic_games = models.CharField(max_length=200)
    steam = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.user.username

