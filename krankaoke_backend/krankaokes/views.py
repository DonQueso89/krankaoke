from rest_framework import mixins, viewsets

from krankaokes import serializers


class KrankaokeViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = serializers.KrankaokeSerializer
    action_serializer_map = {"list": serializers.ListKrankaokeSerializer}

    def get_serializer_class(self):
        return self.action_serializer_map.get(
            self.action, super().get_serializer_class()
        )

    def get_queryset(self):
        return self.request.user.krankaoke_set.all()
