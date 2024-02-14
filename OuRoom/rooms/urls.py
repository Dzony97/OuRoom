from django.urls import path
from . import views

urlpatterns = [
    path('mainroom/', views.main_room, name='main_room'),
    path('ouroom/', views.ouroom, name='ouroom'),
    path('games/', views.games, name='games'),
    path('profile/', views.profile, name='profile'),
]