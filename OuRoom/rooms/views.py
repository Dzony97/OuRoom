from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView, View
from .models import Post, Comment, CommentReply, Group, GroupMembers
from .forms import AddCommentForm, AddCommentReplyForm, AddGroupMemberForm
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q

class PostListView(ListView):

    model = Post
    template_name = 'rooms/mainroom.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        return Post.objects.filter(group__isnull=True) # Take posts that are not in any group

class PostDetailView(DetailView):

    model = Post
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) # get the context for the template
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

class GroupListView(ListView):

    model = Group
    template_name = 'rooms/ouroom.html'
    context_object_name = 'group_list'

    def get_queryset(self):

        user = self.request.user

        return Group.objects.filter(Q(membership__user=user) | Q(author=user)).distinct()
        # Q = allows to combine conditions. Show groups in which you are a member of founder / elimination of duplicates

class GroupCreateView(LoginRequiredMixin, CreateView):

    model = Group
    fields = ['name', 'description']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class GroupDetailView(DetailView):

    model = Group
    context_object_name = 'group'
    template_name = 'rooms/group_detail.html'
    pk_url_kwarg = 'group_id' # Change pk to group_id in url

    def get_object(self, queryset=None):

        group_id = self.kwargs.get(self.pk_url_kwarg)
        self.object = get_object_or_404(Group, id=group_id)
        return self.object
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = AddGroupMemberForm(group_id=self.object.id)
        context['members'] = GroupMembers.objects.filter(group=self.object) #Download all members
        context['post_list'] = Post.objects.filter(group=self.object)
        print(context)
        print('dupa')
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = AddGroupMemberForm(request.POST, group_id=self.object.id)
        if form.is_valid():
            new_member = form.save(commit=False)
            new_member.group = self.get_object()
            new_member.save()
            return redirect(self.get_object().get_absolute_url())
        else:
            return render(request, 'group_detail.html', {'form': form})

class GroupDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):

    model = Group
    success_url = '/'

    def test_func(self):
        group = self.get_object()
        return self.request.user == group.author

class GroupUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Group
    fields = ['name', 'description']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):  # checks whether the current user is the author of this event
        group = self.get_object()
        return self.request.user == group.author

class PostGroupListView(ListView):

    model = Post
    template_name = 'rooms/group_detail.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        group_id = self.kwargs['group_id']
        return Post.objects.filter(group_id=group_id)

class PostGroupCreateView(LoginRequiredMixin, CreateView):

    model = Post
    fields = ['content', 'image']

    def form_valid(self, form):
        group_id = self.kwargs.get('group_id')
        form.instance.author = self.request.user
        group = get_object_or_404(Group, id=group_id)
        form.instance.group = group
        return super().form_valid(form)

class GroupPostDetailView(DetailView):

    model = Post
    context_object_name = 'group_post'

def some_view(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'group_detail.html', {'post': post})

def member_delete(request, group_id, member_id ):

    group = get_object_or_404(Group, id=group_id)
    member = get_object_or_404(GroupMembers, id=member_id, group=group)

    if request.user == member.user or request.user == group.author: #The group leader and member (himself) can remove them from the group
        if request.method == 'POST':
            member.delete()
            return redirect('group_detail', group_id=group_id)

    return render(request, 'rooms/member_delete.html', {'member': member})

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
            return redirect('post_detail', pk=comment.post.pk)

    return redirect('post_detail', pk=comment.post.pk)

@login_required
def comment_reply_delete(request, pk):

    comment_reply = get_object_or_404(CommentReply, id=pk, author=request.user)

    if request.method == 'POST':
        comment_reply.delete()
        return redirect('post_detail', comment_reply.comment.post.id)

    return render(request, 'rooms/comment_reply_delete.html', {'comment_reply': comment_reply})

def main_room(request, pk):

    post = get_object_or_404(Post, id=pk)

    context = {
        'post': post,
    }

    return render(request, 'rooms/mainroom.html', context)

@login_required
def ouroom(request, pk):

    group = get_object_or_404(Group, id=pk)

    context = {
        'group': group,
    }

    return render(request, 'rooms/ouroom.html', context)

@login_required
def games(request):
    return render(request, 'rooms/games.html')

def profile(request):
    return render(request, 'rooms/profile.html')
