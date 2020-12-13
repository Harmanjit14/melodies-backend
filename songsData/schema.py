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
    genre = graphene.List(AllGenre)
    topartists = graphene.List(AllArtist)
    topsongs = graphene.List(AllSongs)
    topgenre = graphene.List(AllGenre)

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

    def resolve_genre(self,info):
        active = info.context.user
        if active.is_anonymous:
            raise GraphQLError("Not Logged In")
        return Genere.objects.all().order_by("-value")