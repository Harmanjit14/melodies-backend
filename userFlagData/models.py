from uuid import uuid4
from django.conf import settings
from django.db import models
from songsData.models import Artist, Song, Genere
# Create your models here.


class UserGenereFlags(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    genere = models.ForeignKey(Genere, on_delete=models.CASCADE)
    value = models.IntegerField(null=True, default=0)

    def save(self, *args, **kwargs):
        super(UserGenereFlags, self).save(*args, **kwargs)

    def __str__(self):
        return self.user.email


class UserArtistFlag(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    value = models.IntegerField(null=True, default=0)

    def save(self, *args, **kwargs):
        super(UserArtistFlag, self).save(*args, **kwargs)

    def __str__(self):
        return self.user.email


class UserLikedList(models.Model):
    id = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super(UserLikedList, self).save(*args, **kwargs)

    def __str__(self):
        return self.user.email
