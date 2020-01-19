from decouple import config
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils.translation import ugettext as _
from django.views import View
from django.views.generic import ListView
from steam.models import Steam

from .models import Genre

class GenreListView(ListView):
    model = Genre
    template_name = 'genre/genre_list.html'


class GenreDeleteView(PermissionRequiredMixin, View):
    permission_required = 'genre.delete_genre'
    raise_exception = True

    def get(self, request, genre_id):
        genre = Genre.objects.get(id=genre_id)
        genre.delete()
        return HttpResponseRedirect(reverse('genre-list'))


class GamesByGenreView(ListView,View):
    """Display all games with selected genre"""
    model = Genre
    def get(self, request, genre_id):
        selected_genre = Genre.objects.get(id=genre_id)
        ctx = {
            'all_games_with_genre': Steam.objects.filter(genre=selected_genre),
            'selected_genre': selected_genre,
            'genres':Genre.objects.all()
        }

        return render(
            request,
            template_name='genre/games_by_genre.html',
            context=ctx
        )