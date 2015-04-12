# from rest_framework import serializers
# from registration.models import Profile
#
#
# class ProfileSerializer(serializers.HyperlinkedModelSerializer):
#     """
#     profile serializer
#     """
#     password = serializers.CharField(write_only=True, required=False)
#     confirm_password = serializers.CharField(write_only=True, required=False)
#
#     def create(self, validated_data):
#         profile = super(ProfileSerializer, self).create(validated_data)
#         profile.set_password(validated_data['password'])
#         profile.save()
#         return profile
#
#     def update(self, instance, validated_data):
#         super(ProfileSerializer, self).update(instance, validated_data)
#         instance.set_password(validated_data['password'])
#         instance.save()
#         return instance
#
#     def validate(self, data):
#         """
#         Checks to be sure that the received password and confirm_password
#         fields are exactly the same
#         """
#         if data['password'] != data.pop('confirm_password'):
#             raise serializers.ValidationError({'password and password_confirm': 'Passwords did not match'})
#         return data
#
#     class Meta:
#         model = Profile
#         fields = ('url', 'username', 'email', 'is_staff', 'password', 'confirm_password',)
