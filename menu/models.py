from django.db import models

# Create your models here.


class Component(models.Model):
    ingredient = models.ForeignKey(
        'story.Ingredient',
        on_delete=models.CASCADE,
    )
    quantity = models.IntegerField(default=1)

    @property
    def name(self):
        return f"{self.ingredient.name} - {self.quantity} {self.ingredient.get_unit_display()}"

    def __str__(self):
        return self.name
