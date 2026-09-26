from rest_framework.serializers import SlugRelatedField, ModelSerializer
from story.serializers import ManagerIngredientSerializer, BaristaIngredientSerializer
from .models import MenuItem, Component


class BaseComponentSerializer(ModelSerializer):
    class Meta:
        model = Component
        fields = '__all__'


class BaseMenuItemSerializer(ModelSerializer):
    class Meta:
        model = MenuItem
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
