from rest_framework.viewsets import ModelViewSet

from authx.permissions import IsCasherUser

from .serializers import (
    PurchaseOrderSerializer,
    CreatePurchaseOrderSerializer
)

from .models import PurchaseOrder


class PurchaseViewSet(ModelViewSet):
    queryset = PurchaseOrder.objects.all()
    permission_classes = [IsCasherUser]

    def get_serializer_class(self):
        if self.action in ['update', 'partial_update', 'create']:
            return CreatePurchaseOrderSerializer
        else:
            return PurchaseOrderSerializer
