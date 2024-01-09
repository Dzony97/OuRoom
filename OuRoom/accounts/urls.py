from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('sign-up/', views.sign_up, name='sign_up'),
    path('login/', views.log_in, name='log_in'),
    path('logout/', views.logout, name='logout'),
]