from django.shortcuts import render, get_object_or_404
from .models import Movie


def home(request):
    movies = Movie.objects.all()
    return render(request, 'movies/home.html', {'movies': movies})


def details(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, 'movies/details.html', {'movie': movie})
