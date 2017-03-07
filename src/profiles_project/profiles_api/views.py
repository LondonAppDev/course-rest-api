from django.shortcuts import render

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import viewsets
# Create your views here.

from . import serializers, models
from profiles_api.permissions import IsOwnerOrReadOnly


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating profiles."""

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsOwnerOrReadOnly,)
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()


class LoginView(ObtainAuthToken):
    """Handles user logins."""

    renderer_classes = (renderers.JSONRenderer, renderers)




class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating profile feeds."""

    authentication_classes = (TokenAuthentication,)
