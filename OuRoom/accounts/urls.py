from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('sign-up/', views.sign_up, name='sign_up'),
    path('login/', views.log_in, name='log_in'),
    path('logout/', views.logout, name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('password_reset/', views.password_reset, name='password_reset'),
]