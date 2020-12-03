from django.db import models
from django.db.models.base import Model

# Create your models here.


class Genere(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    genere = models.CharField(
        unique=True, max_length=250, null=True, blank=True)

    def save(self, *args, **kwargs):
        super(Genere, self).save(*args, **kwargs)

    def __str__(self):
        return self.Genere.genere
