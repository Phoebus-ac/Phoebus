from rest_framework import serializers

from accounts.serializers import CustomUserSerializers

from manuscripts.models import Manuscript


class ManuscriptSerializers(serializers.ModelSerializer):
    author = CustomUserSerializers()

    class Meta:
        model = Manuscript
        fields = ('id', 'title', 'author', 'category', 'timestamp',
                  'is_deleted')
