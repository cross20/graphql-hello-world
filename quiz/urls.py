from django.urls import path
from graphene_django.views import GraphQLView
from quiz.schema import schema

urlpatterns = [
    # Only a single URL to acces GraphQL
    path("quiz", GraphQLView.as_view(graphiql=True, schema=schema)),
]