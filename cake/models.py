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

    class Cream(models.TextChoices):
        ROUND = "round"
        STRIPE = "stripe"
        FLOWER = "flower"

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="usercakes",
    )
    cakeshape = models.CharField(
        choices=Shape.choices,
        max_length=10,
        default=Shape.CIRCLE,
    )
    cakecolor = ColorField(
        default="#ffffff",
        help_text="원하는 색상을 선택하세요.",
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

    image = models.URLField(blank=True, null=True)
    
    lettering = models.CharField(
        max_length=30,
        default="Happy Birthday",
        help_text="케이크 위에 쓰여질 글자를 입력하세요.",
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
    
    # def get_object(self, nickname, password):
    #     try:
    #         return Visitor.objects.get(nickname, password)
    #     except Visitor.DoesNotExist:
    #         return None
    
    class Topping(models.TextChoices):
        STRAWBERRY = "strawberry"
        CHERRY = "cherry"
        SPARKLE = "sparkle"
        HEART = "heart"
        PEARL = "pearl"
        RIBBON = "ribbon"

    usercake = models.ForeignKey(
        UserCake,
        on_delete=models.CASCADE,
        related_name="decocakes",
    )
    
    
    visitor = models.ForeignKey(
        "visitors.Visitor",
        on_delete=models.CASCADE,
        null=True,
        related_name="decocakes",
    )

    toppings = models.CharField(
        max_length=20,
        choices=Topping.choices,
        default="",
    )

    letter = models.TextField(
        max_length=50,
        blank=False,
        null=False,
        help_text="생일 축하 메세지를 입력하세요.",
    )

    def __str__(self) -> str:
        return f"{self.usercake}"

    def __str__(self) -> str:
        return f"{self.visitor}"
    
    def total_letter(self):
        return self.letter.count()
