from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView

urlpatterns = [
    path('', PostListView.as_view(), name='main_room'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('post/new', PostCreateView.as_view(), name='post_new'),
    path('ouroom/', views.ouroom, name='ouroom'),
    path('games/', views.games, name='games'),
]