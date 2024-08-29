from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MovieSerializer
from .models import Moviedata

# Create your views here.
# creating a class-based view
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Moviedata.objects.all()
    serializer_class = MovieSerializer

# creating class-based views for the categories
class ActionViewSet(viewsets.ModelViewSet):
    # query the movie data model for movies with category action
    queryset = Moviedata.objects.filter(typ='action')
    serializer_class = MovieSerializer

class ComedyViewSet(viewsets.ModelViewSet):
    # query the movie data model for movies with category comedy
    queryset = Moviedata.objects.filter(typ='comedy')
    serializer_class = MovieSerializer