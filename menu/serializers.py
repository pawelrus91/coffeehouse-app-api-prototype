from rest_framework.serializers import (
    SlugRelatedField,
    ModelSerializer,
    PrimaryKeyRelatedField,
)
from story.serializers import ManagerIngredientSerializer, BaristaIngredientSerializer
from .models import Menu, MenuItem, Component


class BaseComponentSerializer(ModelSerializer):
    class Meta:
        model = Component
        fields = '__all__'


class BaseMenuItemSerializer(ModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'


class BaseMenuSerializer(ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'


class ManagerComponentSerializer(BaseComponentSerializer):
    ingredient = ManagerIngredientSerializer(read_only=True)


class ComponentSerializer(BaseComponentSerializer):
    ingredient = BaristaIngredientSerializer(read_only=True)


class MenuItemSerializer(BaseMenuItemSerializer):
    ingredients = ComponentSerializer(read_only=True, many=True)


class ManagerMenuItemsSerializer(BaseMenuItemSerializer):
    ingredients = ManagerComponentSerializer(read_only=True, many=True)


class CashierMenuItemSerializer(BaseMenuItemSerializer):
    ingredients = SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )


class MenuSerializer(BaseMenuSerializer):
    items = MenuItemSerializer(read_only=True, many=True)


class AdminMenuSerializer(BaseMenuSerializer):
    items = ManagerMenuItemsSerializer(read_only=True, many=True)


class CashierMenuSerializer(BaseMenuSerializer):
    items = CashierMenuItemSerializer(read_only=True, many=True)


class CreateMenuItemSerializer(BaseMenuItemSerializer):
    ingredients = PrimaryKeyRelatedField(
        many=True,
        queryset=Component.objects.all()
    )


class CreateMenuSerializer(BaseMenuSerializer):
    items = PrimaryKeyRelatedField(
        many=True,
        queryset=MenuItem.objects.all()
    )
