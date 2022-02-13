from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib import admin

class LfgModel(admin.ModelAdmin):    
    def has_add_permission(request) -> bool:
        return True

    def has_change_permission(request, obj=None) -> bool:
        return False

    def has_delete_permission(request, obj=None) -> bool:
        return False

class Videogame(LfgModel):
    name = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    release_date = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.name

class Party(LfgModel):
    name = models.CharField(max_length=200)
    videogame = models.ForeignKey(Videogame,on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.name

class Profile(LfgModel):
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

class Message(LfgModel):
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField()
    deleted = models.BooleanField()
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(default=timezone.now)

    def has_change_permission(request, obj=None) -> bool:
        if not obj: return False

        return settings.AUTH_USER_MODEL == obj.creator

    def has_delete_permission(request, obj=None) -> bool:
        if not obj: return False

        return settings.AUTH_USER_MODEL == obj.creator

    def __str__(self) -> str:
        return self.content