from django.urls import path,url
from . import views
from .views import Gamelist, Steamview


urlpatterns = [
    path('/', views.Gamelist , name='game-list'),
    path('/', Gamelist.as_view() , name='game-list1'),
]