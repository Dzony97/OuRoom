from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import PostListView, PostDetailView, PostCreateView, PostDeleteView, PostUpdateView, PostLike, comment_send, comment_delete

urlpatterns = [
    path('', PostListView.as_view(), name='main_room'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('post/new', PostCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/like', PostLike.as_view(), name='post_like'),
    path('comment/<int:pk>', comment_send, name='comment-post'),
    path('comment/<int:pk>/delete', comment_delete, name='comment_delete'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('ouroom/', views.ouroom, name='ouroom'),
    path('games/', views.games, name='games'),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)