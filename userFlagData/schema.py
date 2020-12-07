from songsData.models import Song
from django.db import models
import graphene
from graphene_django import DjangoObjectType
from songsData.models import Genere, Artist
from .models import UserArtistFlag, UserGenereFlags, UserLikedList
from graphql import GraphQLError


class ArtistF(DjangoObjectType):
    class Meta:
        model = UserArtistFlag


class GenreF(DjangoObjectType):
    class Meta:
        model = UserGenereFlags


class Liked(DjangoObjectType):
    class Meta:
        model = UserLikedList


class AddList(graphene.Mutation):
    add = graphene.Field(Liked)

    class Arguments:
        id = graphene.String()

    def mutate(self, info, id):
        user = info.context.user
        if user.is_anonymous:
            raise GraphQLError("Log in")
        song = Song.objects.get(id=id)
        this = UserLikedList.objects.create(user=user, song=song)

        return AddList(add=this)


class updateGenre(graphene.Mutation):
    update = graphene.Field(GenreF)

    def mutate(self, info):
        user = info.context.user
        if user.is_anonymous:
            raise GraphQLError("Log in")
        my = UserGenereFlags.objects.get(user=user)
        my.value = my.value + 1
        my.save()

        return updateGenre(update=my)


class CreateGenre(graphene.Mutation):
    create = graphene.Field(GenreF)

    class Arguments:
        id = graphene.String()

    def mutate(self, info, id):
        user = info.context.user
        if user.is_anonymous:
            raise GraphQLError("Log in")
        genre = Genere.objects.get(id=id)
        my = UserGenereFlags.objects.create(user=user, genere=genre)
        my.save()
        return CreateGenre(create=my)


class Mutation(graphene.ObjectType):
    add = AddList.Field()
    updateG = updateGenre.Field()
    createG = CreateGenre.Field()
