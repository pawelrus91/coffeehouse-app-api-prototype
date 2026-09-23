from rest_framework.viewsets import ModelViewSet
from authx.permissions import IsBaristaUser

from .serializers import ComponentSerializer, ManagerComponentSerializer
from .models import Component


class ComponentViewSet(ModelViewSet):
    queryset = Component.objects.all()
    permission_classes = [IsBaristaUser]

    def get_serializer_class(self):
        if self.request.user.role >= 3:
            return ManagerComponentSerializer
        else:
            return ComponentSerializer
