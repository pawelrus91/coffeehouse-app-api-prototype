from rest_framework.serializers import (
    ModelSerializer,
    PrimaryKeyRelatedField
)
from menu.serializers import CashierMenuItemSerializer

from .models import PurchaseOrder
from menu.models import MenuItem


class PurchaseOrderSerializer(ModelSerializer):
    items = CashierMenuItemSerializer(many=True)

    class Meta:
        model = PurchaseOrder
        fields = "__all__"


class CreatePurchaseOrderSerializer(PurchaseOrderSerializer):
    items = PrimaryKeyRelatedField(many=True, queryset=MenuItem.objects.all())
