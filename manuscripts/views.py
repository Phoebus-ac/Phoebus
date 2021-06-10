from rest_framework import viewsets

from manuscripts.models import Manuscript
from manuscripts.serializers import ManuscriptSerializers


class ManuscriptView(viewsets.ModelViewSet):
    lookup_url_kwarg = 'id'
    queryset = Manuscript.objects.all()

    def get_serializer_class(self):
        return ManuscriptSerializers

    def filter_queryset(self, queryset):
        queryset = self.get_queryset().filter(creator=self.request.user)
        return queryset
