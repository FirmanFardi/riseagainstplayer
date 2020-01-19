from django.urls import path

from .views import  GenreListView,GenreDeleteView,GamesByGenreView
from .import views


urlpatterns = [

    path('genre_list/', GenreListView.as_view(),
         name='genre-list'),
    path('genre_delete/<genre_id>', GenreDeleteView.as_view(),
         name='genre-delete'),
    path('games_by_genre/<genre_id>', GamesByGenreView.as_view(),
         name='games-by-genre')
]