from django.db import models
import graphene
from graphene_django import DjangoObjectType
from .models import Genere, Song, Artist
from graphql import GraphQLError


class AllArtist(DjangoObjectType):
    class Meta:
        model = Artist


class AllSongs(DjangoObjectType):
    class Meta:
        model = Song


class AllGenre(DjangoObjectType):
    class Meta:
        model = Genere


class Query(graphene.ObjectType):
    artists = graphene.List(AllArtist)
    songs = graphene.List(AllSongs)

    def resolve_artists(self, info):
        active = info.context.user
        if active.is_anonymous:
            raise GraphQLError("Not Logged In")
        return Artist.objects.all().order_by("-artist")

    def resolve_songs(self, info):
        active = info.context.user
        if active.is_anonymous:
            raise GraphQLError("Not Logged In")
        return Song.objects.all().order_by("-title")
