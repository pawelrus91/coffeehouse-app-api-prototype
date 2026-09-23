from django.urls.conf import include
from django.urls import re_path

from rest_framework.routers import DefaultRouter

from .viewsets import ComponentViewSet

router = DefaultRouter()
router.register(
    r'components',
    ComponentViewSet,
    basename='menu',
)


urlpatterns = [
    re_path(r'', include(router.urls)),
]
