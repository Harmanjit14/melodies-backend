from django.contrib import admin
from .models import UserArtistFlag, UserGenereFlags, UserLikedList

# Register your models here.
admin.site.register(UserLikedList)
admin.site.register(UserArtistFlag)
admin.site.register(UserGenereFlags)
