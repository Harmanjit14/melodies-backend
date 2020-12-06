from uuid import uuid4
from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE

# Create your models here.


class Genere(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    genere = models.CharField(
        max_length=250, null=True, blank=True)
    image = models.URLField(max_length=255, null=True, blank=True)
    value = models.IntegerField(null=True, default=0)

    def save(self, *args, **kwargs):
        super(Genere, self).save(*args, **kwargs)

    def __str__(self):
        return self.genere


class Artist(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    artist = models.CharField(max_length=250, blank=True, null=True)
    image = models.URLField(max_length=255, null=True, blank=True)

    def save(self, *args, **kwargs):
        super(Artist, self).save(*args, **kwargs)

    def __str__(self):
        return self.artist


class Song(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    title = models.CharField(null=True, blank=True, max_length=250)
    genere = models.ForeignKey(Genere, on_delete=CASCADE)
    artist = models.ForeignKey(Artist, on_delete=CASCADE)
    image = models.URLField(blank=True, null=True, max_length=255)
    link = models.URLField(blank=True, null=True, max_length=255)
    value = models.IntegerField(null=True, default=0)

    def save(self, *args, **kwargs):
        super(Song, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
