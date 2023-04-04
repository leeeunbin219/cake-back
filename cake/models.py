from colorfield.fields import ColorField

from django.db import models
from users.models import User
from visitors.models import Visitor


# 생일자의 케이크 기본 설정
class UserCake(models.Model):
    class Shape(models.TextChoices):
        CIRCLE = "circle"
        SQUARE = "square"
        HEART = "heart"
        

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="usercakes",
    )
    shape = models.CharField(
        choices=Shape.choices,
        max_length=10,
        default=Shape.CIRCLE,
    )
    color = ColorField(
        default="#ffffff",
        help_text="원하는 색상을 선택하세요.",
    )
    image = models.URLField(blank=True, null=True)
    lettering = models.CharField(
        max_length=30,
        default="Happy Birthday",
    )

    visitor = models.ManyToManyField(
        "visitors.Visitor",
        related_name="usercakes",
    )

    def __str__(self) -> str:
        return f"{self.user}"

    def total_visitor(self):
        return self.visitor.count()


# visitor 가 꾸며주는 생일자의 케이크
class DecoCake(models.Model):
    class Cream(models.TextChoices):
        ROUND = "round"
        STRIPE = "stripe"
        FLOWER = "flower"

    usercake = models.ForeignKey(
        UserCake,
        on_delete=models.CASCADE,
        related_name="decocakes",
    )

    cream = models.CharField(
        choices=Cream.choices,
        max_length=10,
        default=Cream.ROUND,
    )

    creamcolor = ColorField(
        default="#ffffff",
        help_text="원하는 색상을 선택하세요.",
    )

    visitor = models.ForeignKey(
        "visitors.Visitor",
        on_delete=models.CASCADE,
        null=True,
        related_name="decocakes",
    )

    letter = models.TextField(
        max_length=50,
        blank=False,
        null=False,
    )

    def __str__(self) -> str:
        return f"{self.usercake}"
    