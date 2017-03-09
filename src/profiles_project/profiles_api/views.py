from django.shortcuts import render

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets, renderers
# Create your views here.

from . import serializers, models
from profiles_api.permissions import IsOwnerOrReadOnly


class HelloApiView(APIView):
    """Test API View."""

    def get(self, request, format=None):
        """Return a hello message."""

        return Response({'viewtype': 'apiview'})


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet."""

    def list(self, request):
        """Return a hello message."""

        return Response({'view-type': 'viewset'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating profiles."""

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsOwnerOrReadOnly,)
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()


class LoginViewSet(viewsets.ViewSet):
    """Handles creating and returning user authentication tokens."""

    serializer_class = AuthTokenSerializer

    def create(self, request):
        """Check the email and password and return an auth token."""

        return ObtainAuthToken().post(request)


class LoginView(ObtainAuthToken):
    """Handles user logins."""

    renderer_classes = (renderers.JSONRenderer, renderers.BrowsableAPIRenderer)


class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating profile feeds."""

    authentication_classes = (TokenAuthentication,)
