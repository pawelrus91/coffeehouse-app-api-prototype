from django.urls.conf import include
from django.urls import re_path

from rest_framework.routers import DefaultRouter

from .viewsets import (
    MenuViewSet,
    MenuItemViewSet,
    ComponentViewSet
)

router = DefaultRouter()

router.register(
    r'menu',
    MenuViewSet,
    basename="menu",
)
router.register(
    r'items',
    MenuItemViewSet,
    basename="items",
)
router.register(
    r'components',
    ComponentViewSet,
    basename="components",
)

urlpatterns = [
    re_path(r'', include(router.urls)),
]
