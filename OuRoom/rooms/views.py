from django.shortcuts import render
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from .models import Post

class PostListView(ListView):

    model = Post
    template_name = 'rooms/mainroom.html'
    context_object_name = 'post_list'

class PostDetailView(DetailView):

    model = Post

class PostCreateView(CreateView):

    model = Post
    fields = ['content', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

def main_room(request):

    context = {
        'post_list': Post.objects.all()
    }

    return render(request, 'rooms/mainroom.html', context)

def ouroom(request):
    return render(request, 'rooms/ouroom.html')

def games(request):
    return render(request, 'rooms/games.html')

def profile(request):
    return render(request, 'rooms/profile.html')
