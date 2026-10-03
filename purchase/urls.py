from django.urls.conf import include
from django.urls import re_path

from rest_framework.routers import DefaultRouter

from .viewsets import PurchaseViewSet

router = DefaultRouter()
router.register(
    r'purchase',
    PurchaseViewSet,
    basename='purchase',
)


urlpatterns = [
    re_path(r'', include(router.urls)),
]
