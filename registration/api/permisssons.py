# from rest_framework import permissions
# from registration.models import Profile
#
#
# class IsOwnerOrReadOnly(permissions.BasePermission):
#     """
#     Custom permission to only allow owners of an object to edit it.
#     """
#
#     def has_object_permission(self, request, view, obj):
#         """
#         Provides SAFE_METHODS access to the actions
#         returns true if the user matches the owner of the user
#         """
#         if request.method in permissions.SAFE_METHODS:
#             return True
#
#         """
#         check if the profile of objects
#         matches the request user
#         """
#         if isinstance(obj, Profile):
#             return obj == request.user
#         return obj.profile == request.user
