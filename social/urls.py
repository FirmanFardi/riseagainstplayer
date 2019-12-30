from django.urls import path
from django.conf.urls import url
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from .import views

urlpatterns = [
    path('', PostListView.as_view(), name='social-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='social-about'),
    path('recommender/', views.recommender, name='social-recommender'),
    url(r'^ajax/select_invoice/$', views.select_invoice, name='select_invoice'),
    path('', views.PersonListView.as_view(), name='person_changelist'),
    path('recommender/add/', views.PersonCreateView.as_view(), name='person_add'),
    path('<int:pk>/', views.PersonUpdateView.as_view(), name='person_change'),
]




