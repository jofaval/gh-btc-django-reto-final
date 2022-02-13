from dataclasses import fields
from rest_framework import serializers
from .models import *

class VideogameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Videogame
        fields = ('name', 'genre', 'release_date')

class PartySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Party
        fields = ('name', 'videogame', 'created_date')

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ('user', 'twitter', 'instagram', 'telegram', 'website', 'twitch', 'epic_games', 'steam')

class MessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Message
        fields = ('creator', 'content', 'deleted', 'created_date', 'updated_date')