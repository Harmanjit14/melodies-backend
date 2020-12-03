from django.contrib import admin
from .models import Genere, Song, Artist

# Register your models here.
admin.site.register(Genere)
admin.site.register(Song)
admin.site.register(Artist)
