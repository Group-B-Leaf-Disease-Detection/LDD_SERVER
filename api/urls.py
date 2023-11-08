from plants.views import PlantDiseaseDetectionViewSet

from django_rest_passwordreset.views import \
    ResetPasswordValidateTokenViewSet, \
    ResetPasswordConfirmViewSet, \
    ResetPasswordRequestTokenViewSet

from auths.views import \
    ServerStatusViewSet, \
    UserRegistrationViewSet, \
    UserLoginViewSet, \
    UserDetailsViewSet, \
    UserChangePasswordViewSet, \
    UserActivationViewSet

from drf_yasg import openapi
from django.conf import settings
from django.urls import path, include
from drf_yasg.views import get_schema_view
from django.conf.urls.static import static
from rest_framework import routers, permissions

from django.conf.urls import (
    handler404, 
    handler500,
  )

schema_view = get_schema_view(
   openapi.Info(
      title="SmartKrishi API",
      default_version='v1',
      description="Leafe Disease Detection API",
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

router = routers.DefaultRouter()

router.register(
    r'status',
    ServerStatusViewSet,
    basename='status'
)

router.register(
    r'register',
    UserRegistrationViewSet,
    basename='register'
)

router.register(
    r'activate',
    UserActivationViewSet,
    basename='activate'
)

router.register(
    r'login',
    UserLoginViewSet,
    basename='login'
)

router.register(
    r'forgot-password',
    ResetPasswordRequestTokenViewSet,
    basename='forgot-password'
)

router.register(
    r'validate_token',
    ResetPasswordValidateTokenViewSet,
    basename='validate-token'
)

router.register(
    r'reset-password',
    ResetPasswordConfirmViewSet,
    basename='reset-password'
)

router.register(
    r'profile',
    UserDetailsViewSet,
    basename='profile'
)

router.register(
    r'change-password',
    UserChangePasswordViewSet,
    basename='change-password'
)

router.register(
    r'plant-disease-detection',
    PlantDiseaseDetectionViewSet,
    basename='plant-disease-detection'
)


urlpatterns = [
    path('', include(router.urls)),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = 'api.views.error404'
handler500 = 'api.views.error500'