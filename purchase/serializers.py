from rest_framework.serializers import (
    ModelSerializer,
    PrimaryKeyRelatedField,
    CharField,
)
from menu.serializers import CashierMenuItemSerializer

from .models import PurchaseOrder
from menu.models import MenuItem


class ListPurchaseOrderSerializer(ModelSerializer):
    status = CharField(source="get_status_display")

    class Meta:
        model = PurchaseOrder
        fields = ["status", "order_name"]


class PurchaseOrderSerializer(ModelSerializer):
    items = CashierMenuItemSerializer(many=True)

    class Meta:
        model = PurchaseOrder
        fields = "__all__"


class CreatePurchaseOrderSerializer(PurchaseOrderSerializer):
    items = PrimaryKeyRelatedField(many=True, queryset=MenuItem.objects.all())
