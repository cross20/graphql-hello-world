from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView
from users.schema import schema

urlpatterns = [
    path('users', csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema, middleware='graphql_jwt.middleware.JSONWebTokenMiddleware'))),
]