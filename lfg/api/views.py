from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import *

# Create your views here.
class VideogameViewSet():
    queryset = Videogame.objects.all().order_by('name')
    serializer_class = VideogameSerializer

class PartyViewSet():
    queryset = Party.objects.all().order_by('name')
    serializer_class = PartySerializer

class ProfileViewSet():
    queryset = Profile.objects.all().order_by('user.name')
    serializer_class = ProfileSerializer

class MessageViewSet():
    queryset = Message.objects.all().order_by('created_date')
    serializer_class = MessageSerializer
