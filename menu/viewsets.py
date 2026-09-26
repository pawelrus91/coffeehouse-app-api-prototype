from rest_framework.viewsets import ModelViewSet
from authx.permissions import IsCasherUser, IsBaristaUser

from .serializers import (
    MenuItemSerializer,
    CashierMenuItemSerializer,
    ManagerMenuItemsSerializer,
    ComponentSerializer,
    ManagerComponentSerializer
)
from .models import MenuItem, Component


class MenuItemViewSet(ModelViewSet):
    queryset = MenuItem.objects.all()
    permission_classes = [IsCasherUser]

    def get_serializer_class(self):
        if self.request.user.role == 1:
            return CashierMenuItemSerializer
        elif self.request.user.role >= 3:
            return ManagerMenuItemsSerializer
        else:
            return MenuItemSerializer


class ComponentViewSet(ModelViewSet):
    queryset = Component.objects.all()
    permission_classes = [IsBaristaUser]

    def get_serializer_class(self):
        if self.request.user.role >= 3:
            return ManagerComponentSerializer
        else:
            return ComponentSerializer
