from django.contrib.auth.models import Group, User
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import mixins, response, viewsets
from rest_framework.decorators import action

from users.serializers import CreateUserSerializer, UserSerializer


class UserViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer

    @swagger_auto_schema(
        method="get",
        responses={
            200: openapi.Response(
                description="Introspect the logged in user",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={"id": openapi.Schema(type=openapi.TYPE_NUMBER)},
                ),
            )
        },
    )
    @action(methods=["get"], detail=False)
    def me(self, request):
        return response.Response(data={"id": request.user.id})


class CreateUserViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer
