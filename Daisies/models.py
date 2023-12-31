from django.db import models
from django.contrib.auth.models import User # Import Django's User model

# Create your models here.
# Model for Band Members
class BandMember(models.Model):
    """
    Model representing a band members.
    """
    name = models.CharField(max_length=100)
    role_band = models.CharField(max_length=100)
    bio = models.TextField()
    image = models.ImageField(upload_to='band_members/', default='BAND/static/images/', blank=True, null=True)

    def __str__(self):
        """
        String representation of the band members.
        """
        return self.name
    
# Model for Albums
class Album(models.Model):
    """
    Model representing an album.
    """
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)
    release_date = models.DateField()
    cover_image = models.ImageField(upload_to='album/')

    def __str__(self):
        """
        String representaion of the album.
        """
        return self.title
    
# Model for songs
class Song(models.Model):
    """
    Model representing a song.
    """
    title = models.CharField(max_length=200)
    length = models.DurationField()

    def __str__(self):
        """
        String representation of the song.
        """
        return self.title





