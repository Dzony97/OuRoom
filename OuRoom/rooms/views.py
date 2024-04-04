from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView, View
from .models import Post, Comment
from .forms import AddCommentForm, AddCommentReplyForm
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class PostListView(ListView):

    model = Post
    template_name = 'rooms/mainroom.html'
    context_object_name = 'post_list'

class PostDetailView(DetailView):

    model = Post
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['commentform'] = AddCommentForm()
        context['commentreplyform'] = AddCommentReplyForm()
        return context

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

    def post(self, request, pk):

        post = Post.objects.get(pk=pk)
        user_liked = post.like.filter(pk=request.user.pk).exists()


        if user_liked:
            post.like.remove(request.user)
            liked = False
        else:
            post.like.add(request.user)
            liked = True
            
        return JsonResponse({'liked': liked, 'likes_count': post.like.all().count()})

@login_required
def comment_send(request, pk):
    post = get_object_or_404(Post, id=pk)

    if request.method == "POST":
        form = AddCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False) # The objects isn't immediately saved in the database
            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=pk)

    return redirect('post_detail', pk=pk)

@login_required
def comment_delete(request, pk):

    comment = get_object_or_404(Comment, id=pk, author=request.user)

    if request.method == 'POST':
        comment.delete()
        return redirect('post_detail', comment.post.id)

    return render(request, 'rooms/comment_delete.html', {'comment': comment})

@login_required
def comment_reply_send(request, pk):
    comment = get_object_or_404(Comment, id=pk)

    if request.method == "POST":
        form = AddCommentReplyForm(request.POST)
        if form.is_valid():
            comment_reply = form.save(commit=False)
            comment_reply.author = request.user
            comment_reply.comment = comment
            comment_reply.save()
            return redirect('post_detail', pk=pk)

    return redirect('post_detail', pk=pk)

def main_room(request, pk):

    post = get_object_or_404(Post, id=pk)

    context = {
        'post': post,
    }

    return render(request, 'rooms/mainroom.html', context)

@login_required
def ouroom(request):
    return render(request, 'rooms/ouroom.html')

@login_required
def games(request):
    return render(request, 'rooms/games.html')

def profile(request):
    return render(request, 'rooms/profile.html')
