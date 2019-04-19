from rest_framework import viewsets, mixins
from ..models import Songs
from ..serializers import SongsSerializer


class SongsViewSet(viewsets.ReadOnlyModelViewSet, mixins.RetrieveModelMixin):
    queryset = Songs.objects.all()
    serializer_class = SongsSerializer
