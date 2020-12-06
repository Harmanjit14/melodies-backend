import graphene
from graphene_django import DjangoObjectType
from .models import User
from graphql import GraphQLError


class UserType(DjangoObjectType):
    class Meta:
        model = User


class Query(graphene.ObjectType):
    user = graphene.Field(UserType)

    def resolve_user(self, info):
        active = info.context.user
        if active.is_anonymous:
            raise GraphQLError("Not Logged In")
        return active


class CreateUser(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        email = graphene.String(required=True)
        name = graphene.String(required=True)
        password = graphene.String(required=True)

    def mutate(self, info, **kwargs):
        user = User(email=kwargs.get("email"))
        user.name = kwargs.get("name")
        user.set_password(kwargs.get("password"))
        user.save()

        return CreateUser(user=user)


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
