"""Custom REST API Permission Classes.

Learn more here: http://www.django-rest-framework.org/api-guide/permissions/
"""

from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Only allow users to editor their own profile.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id
