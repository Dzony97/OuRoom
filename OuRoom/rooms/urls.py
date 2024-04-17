from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.PostListView.as_view(), name='main_room'),
    path('post/<int:pk>', views.PostDetailView.as_view(), name='post_detail'),
    path('post/new', views.PostCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/like', views.PostLike.as_view(), name='post_like'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
    path('comment/<int:pk>', views.comment_send, name='comment_post'),
    path('comment/<int:pk>/delete', views.comment_delete, name='comment_delete'),
    path('comment/<int:pk>/reply', views.comment_reply_send, name='comment_reply'),
    path('comment/<int:pk>/reply/delete', views.comment_reply_delete, name='comment_reply_delete'),
    path('ouroom/', views.GroupListView.as_view(), name='ouroom'),
    path('ouroom/create', views.GroupCreateView.as_view(), name='create_group'),
    path('ouroom/group/<int:group_id>', views.GroupDetailView.as_view(), name='group_detail'),
    path('ouroom/group/<int:pk>/delete', views.GroupDeleteView.as_view(), name='group_delete'),
    path('games/', views.games, name='games'),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)