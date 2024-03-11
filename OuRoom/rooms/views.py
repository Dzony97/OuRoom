from django.shortcuts import render
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView, View
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class PostListView(ListView):

    model = Post
    template_name = 'rooms/mainroom.html'
    context_object_name = 'post_list'

class PostDetailView(DetailView):

    model = Post
    context_object_name = 'post'

class PostCreateView(LoginRequiredMixin, CreateView):

    model = Post
    fields = ['content', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user # new or update post automatically assigned author.
        return super().form_valid(form) # saving the form instance to the database and redirecting to a specific success URL.

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):

    model = Post
    success_url = '/'

    def test_func(self): #checks whether the current user is the author of this event
        post = self.get_object()
        return self.request.user == post.author

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):

    model = Post
    fields = ['content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self): #checks whether the current user is the author of this event
        post = self.get_object()
        return self.request.user == post.author

class PostLike(LoginRequiredMixin, View):

    def like_post(self, request, pk, *args, **kwargs):

        post = Post.objects.get(pk=pk)
        is_like = False

        for like in post.like.all():
            if like == request.user:
                is_like = True
                break

        if not is_like:
            post.like.add(request.user)

        if is_like:
            post.like.remove(request.user)

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
