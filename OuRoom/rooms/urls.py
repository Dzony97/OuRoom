from django.urls import path
from . import views
from .views import PostListView, PostDetailView

urlpatterns = [
    path('', PostListView.as_view(), name='main_room'),
    path('post_detail', PostDetailView.as_view(), name='post_detail'),
    path('ouroom/', views.ouroom, name='ouroom'),
    path('games/', views.games, name='games'),
]