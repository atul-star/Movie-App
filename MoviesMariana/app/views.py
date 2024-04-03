# Create your views here.
from django.shortcuts import render
from .models import Movie
from .forms import GenreFilterForm


def movie_list(request):
    try:
        movies = Movie.objects.all()
        genre_filter_form = GenreFilterForm(request.GET)

        if genre_filter_form.is_valid():
            genre = genre_filter_form.cleaned_data['genre']
            if genre:
                movies = movies.filter(genres__contains=genre)

        return render(request, 'movie_list.html', {'movies': movies, 'genre_filter_form': genre_filter_form})

    except Exception as e:
        return render(request,'error_page.html', {'error': str(e)})
