from rest_framework.serializers import ModelSerializer
from story.serializers import ManagerIngredientSerializer, BaristaIngredientSerializer
from .models import Component


class BaseComponentSerializer(ModelSerializer):
    class Meta:
        model = Component
        fields = '__all__'


class ManagerComponentSerializer(BaseComponentSerializer):
    ingredient = ManagerIngredientSerializer(read_only=True)


class ComponentSerializer(BaseComponentSerializer):
    ingredient = BaristaIngredientSerializer(read_only=True)
