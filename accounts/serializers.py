from rest_framework import serializers

from accounts.models import CustomUser, Profile


class CustomUserSerializers(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'first_name', 'last_name', 'date_joined',
                  'last_login', 'is_certified')


class ProfileSerializers(serializers.ModelSerializer):
    user = CustomUserSerializers()

    class Meta:
        model = Profile
        fields = ('id', 'user', 'email_verified', 'reputation_tier',
                  'academic_affiliation', 'academic_affiliation_verified',
                  'orcid_id', 'orcid_id_verified')
