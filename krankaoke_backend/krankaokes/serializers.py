import json
from rest_framework import serializers

from krankaokes.models import Krankaoke


class ListKrankaokeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Krankaoke
        fields = ["id", "artist", "title", "user"]


def validate_timings(value):
    value = json.loads(value)
    value = sorted([(w, s, e) for w, (s, e) in value.items()], key=lambda k: k[1])

    last_word, last_end = 0, -1
    for word, start, end in value:
        if start >= end:
            raise serializers.ValidationError(
                f"end time for '{word}' must be smaller than start"
            )
        if last_end >= start:
            raise serializers.ValidationError(
                f"{word} and {last_word} overlap with eachother"
            )


class KrankaokeSerializer(serializers.ModelSerializer):
    timings = serializers.JSONField(validators=[validate_timings], required=False)

    class Meta:
        model = Krankaoke
        fields = ["artist", "title", "audio", "user", "timings"]
