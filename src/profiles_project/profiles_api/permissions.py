"""Custom REST API Permission Classes.

Learn more here: http://www.django-rest-framework.org/api-guide/permissions/
"""

from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """
    Only allow users to edit their own profile.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id


class PostOwnStatus(permissions.BasePermission):
    """
    Only allow users to update their own status.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile.id == request.user.id
