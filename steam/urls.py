from django.urls import path
from . import views
from .views import Gamelist

urlpatterns = [
    path('gamelist/', views.Gamelist , name='game-list')
    path('gamelist/', Gamelist.as_view() , name='game-list1')
]