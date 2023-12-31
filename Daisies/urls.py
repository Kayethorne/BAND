from django.urls import path
from . import views

app_name = 'Daisies'

urlpatterns = [
    path('homepage/', views.homepage, name='homepage'),
    path('band_members/', views.band_members, name='band_members'),
    path('albums/', views.albums, name='albums'),
    path('songs/', views.songs, name='songs'),
]



