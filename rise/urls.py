"""rise URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('social/', include('social.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views

from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

from steam.views import steam
from steam.views import Gamelist,Steamview,Privilege,SteamListView,SteamDeleteView
from genre.views import GenreListView,GenreDeleteView,GamesByGenreView
from developer.views import DeveloperListView, DeveloperDeleteView
from recommendation.views import RecommendGamesManuallyView,RecommendByRatedGamesView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('steam/', steam, name='steam'),
    path('', Gamelist, name='gamelist'),
    path('privelege',Privilege,name='privilege'),
    path('recommendation', RecommendGamesManuallyView.as_view(), name='recommendation'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('social/', include('social.urls')),
    path('genre_list/', GenreListView.as_view(),name='genre-list'),
    path('genre_delete/<genre_id>', GenreDeleteView.as_view(),name='genre-delete'),
    path('games_by_genre/<genre_id>', GamesByGenreView.as_view(),name='games-by-genre'),
    path('recommend_game_by_rating', RecommendByRatedGamesView.as_view(),name='recommend-by-rating'),
    path('developer_list/', DeveloperListView.as_view(),name='developer-list'),
    path('developer_delete/<developer_id>', DeveloperDeleteView.as_view(),name='developer-delete'),
    path('steam_list/', SteamListView.as_view(),name='steam-list'),
    path('steam_delete/<steam_id>', SteamDeleteView.as_view(),name='steam-delete'),

]

if settings.DEBUG:

    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


