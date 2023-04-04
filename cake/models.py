from colorfield.fields import ColorField

from django.db import models
from users.models import User


class UserCake(models.Model):

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="usercakes",
    )
    color = ColorField(default="#ffffff",help_text="원하는 색상을 선택하세요.")
    image = models.URLField(blank=True, null=True)
    lettering = models.CharField(max_length=30, default="Happy Birthday")

    def __str__(self) -> str:
        return f"{self.user}"
    
    
class Topping(models.Model):
    
    class CreamChoices(models.TextChoices):
        FLOWER = "flower", "Flower"
        WAVE = "wave", "Wave"
        ROUND = "round", "Round"
    
    class ToppingChoices(models.TextChoices):
        RIBBON = "ribbon", "Ribbon"
        SPRINKLES = "sprinkles", "Sprinkles"
        COLOR = "color", "Color"
        CHERRY = "cherry", "Cherry"
        SPARKLES = "sparkles", "Sparkles"
        HEART = "heart", "Heart"
        CREAM = "cream", "Cream"

    cream = models.CharField(max_length=20, choices=CreamChoices.choices, default="")
    topping = models.CharField(max_length=20, choices=ToppingChoices.choices, default="")
    
    class Meta:
        verbose_name = "Topping"
        verbose_name_plural = "Toppings"
        
    def __str__(self):
        return f"{self.topping}"