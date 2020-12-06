from uuid import uuid4
from django.conf import settings
from django.db import models
from songsData.models import Song, Genere
# Create your models here.


class UserGenereFlags(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    genere = models.ForeignKey(Genere, on_delete=models.CASCADE)
    value = models.IntegerField(blank=True, null=True)

    def save(self, *args, **kwargs):
        super(UserGenereFlags, self).save(*args, **kwargs)

    def __str__(self):
        return self.user.email


class 
