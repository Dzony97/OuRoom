from django.urls import path
from . import views

urlpatterns = [
    path('mainroom/', views.main_room, name='main_room'),
    path('ouroom/', views.main_room, name='ouroom'),
]