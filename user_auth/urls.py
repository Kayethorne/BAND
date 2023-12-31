from django.urls import path
from . import views

app_name = 'user_auth'

urlpatterns = [
    path('user_login/', views.user_login, name='user_login'),
    path('', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('user_logout/', views.user_logout, name='user_logout'),
]
