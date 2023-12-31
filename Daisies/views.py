from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth import login, authenticate
from .models import BandMember, Album, Song
from django.contrib.auth.decorators import login_required
# Create your views here.

# listing band members
def band_members(request):
    """
    View function for displaying band members.
    """
    band_members = BandMember.objects.all()
    return render(request, 'daisies/band_members.html', {'band_members': band_members})

# listing albums
def albums(request):
    """
    View function for displaying albums.
    """
    albums = Album.objects.all()
    return render(request, 'daisies/albums.html', {'albums': albums})

# listing songs
def songs(request):
    """
    View function for displaying songs.
    """
    songs = Song.objects.all()
    return render(request, 'daisies/songs.html', {'songs': songs})

# Homepage view
@login_required(login_url="/user_auth/login/")
def homepage(request):
    return render(request, 'daisies/homepage.html')


