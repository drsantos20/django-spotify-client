from rest_framework import serializers
from ..models import Songs


class SongsSerializer(serializers.ModelSerializer):

    title = serializers.CharField(required=True)
    artist = serializers.CharField(required=True)

    class Meta:
        model = Songs
        fields = ['title', 'artist']