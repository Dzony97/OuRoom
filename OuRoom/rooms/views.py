from django.shortcuts import render
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from .models import Post

class PostListView(ListView):

    model = Post
    template_name = 'rooms/mainroom.html'
    context_object_name = 'post_list'
    ordering = ['-data_posts']

class PostDetailView(DetailView):
    model = Post



def main_room(request):
    return render(request, 'rooms/mainroom.html')

def ouroom(request):
    return render(request, 'rooms/ouroom.html')

def games(request):
    return render(request, 'rooms/games.html')

def profile(request):
    return render(request, 'rooms/profile.html')
