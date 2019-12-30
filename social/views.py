from django.shortcuts import render
from steam.models import Steam
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView,DetailView,CreateView,UpdateView, DeleteView
from .models import Post
from django.db import connection
from django.http import HttpResponse
from django.http import JsonResponse
from django.urls import reverse_lazy
from .models import Form


def home(request):
    context ={
        'posts': Post.objects.all()
    }
    return render(request, 'social/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'social/home.html' #ni dia cari <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):

    model = Post
    fields = ['title','content']

    def form_valid(self, form):
        form.instance.author = self.request.user #set the form to the current logged in author
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    
    model = Post
    fields = ['title','content']

    def form_valid(self, form):
        form.instance.author = self.request.user #set the form to the current logged in author
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url ='/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def about(request):
    return render(request, 'social/about.html', {'title':'About'})

def recommender(request):

    context = {
        'steams': Steam.objects.all()
        }
    return render(request, 'social/recommender.html',context)

def select_invoice(request):
    gametitle =  request.POST.get('checks')
    cursor = connection.cursor()
    cursor.execute('''SELECT * from db.sqlite3 where gametitle IN('%s')''' %(gametitle))
    row = cursor.fetchall()
    data =  {
            'row': row
        }
    return JsonResponse(data)
    
class PersonListView(ListView):
    model = Form
    context_object_name = 'people'

class PersonCreateView(CreateView):
    model = Form
    fields = ('genre',)
    success_url = reverse_lazy('person_changelist')
    

class PersonUpdateView(UpdateView):
    model = Form
    fields =('genre',)
    success_url = reverse_lazy('person_changelist')

# Create your views here.
