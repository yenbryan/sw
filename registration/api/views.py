# from rest_framework import viewsets
# from registration.api.permisssons import IsOwnerOrReadOnly
# from registration.api.serializers import ProfileSerializer
# from registration.models import Profile
#
#
# class ProfileViewSet(viewsets.ModelViewSet):
#     """
#     profile view set
#     """
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializer
#     permission_classes = (IsOwnerOrReadOnly,)
#
#     """
#     permission_classes = IsOwnerOrReadOnly
#     to protect others from modifying your data
#     """
