from rest_framework import serializers
from krankaokes.models import Krankaoke


class ListKrankaokeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Krankaoke
        fields = ['id', 'artist', 'title', 'user']


class KrankaokeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Krankaoke
        fields = ['artist', 'title', 'audio', 'user']
