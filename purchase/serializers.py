from datetime import datetime
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
    def to_internal_value(self, data):
        today = datetime.now()
        count_date = PurchaseOrder.objects.filter(
            created_date__date=today).count() + 1
        data['order_number'] = f"{today.strftime('%d%m%y')}_{count_date}"

        return super(PurchaseOrderSerializer, self).to_internal_value(data)

    items = PrimaryKeyRelatedField(many=True, queryset=MenuItem.objects.all())
