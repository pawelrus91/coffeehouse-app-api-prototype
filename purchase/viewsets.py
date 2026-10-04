from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny

from authx.permissions import IsCasherUser

from .serializers import (
    PurchaseOrderSerializer,
    CreatePurchaseOrderSerializer,
    ListPurchaseOrderSerializer,
)

from .models import PurchaseOrder


class PurchaseListView(ListAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = ListPurchaseOrderSerializer
    permission_classes = [AllowAny]


class PurchaseViewSet(ModelViewSet):
    queryset = PurchaseOrder.objects.all()
    permission_classes = [IsCasherUser]

    def get_serializer_class(self):
        if self.action in ['update', 'partial_update', 'create']:
            return CreatePurchaseOrderSerializer
        else:
            return PurchaseOrderSerializer
