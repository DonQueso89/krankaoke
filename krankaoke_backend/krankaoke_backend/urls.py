"""krankaoke_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers, permissions
from rest_framework.authtoken import views as drf_views

from users import views as user_views
from krankaokes import views as krankaoke_views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


schema_view = get_schema_view(
   openapi.Info(
      title="Krankaoke API",
      default_version='v1',
      description="Generic backend for Krankaoke apps",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="kg.v.ekeren@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

router = routers.DefaultRouter()
router.register(r"users", user_views.UserViewSet)
router.register(r"users", user_views.CreateUserViewSet)
router.register(r"krankaokes", krankaoke_views.KrankaokeViewSet, basename="krankaokes")


api_token_params = [
    openapi.Parameter('username', openapi.IN_BODY, type=openapi.TYPE_STRING),
    openapi.Parameter('password', openapi.IN_BODY, type=openapi.TYPE_STRING),
]

api_token_view = swagger_auto_schema(method='post', manual_parameters=api_token_params)(drf_views.obtain_auth_token)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include(router.urls)),
    path("api_token/", api_token_view),
    path("swagger/", schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
