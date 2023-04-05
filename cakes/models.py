from colorfield.fields import ColorField
from django.core.validators import RegexValidator

from django.db import models
from users.models import User


# 생일자의 케이크 기본 설정 (UserCake)
class CakeBase(models.Model):
    class Shape(models.TextChoices):
        CIRCLE = "circle"
        SQUARE = "square"
        HEART = "heart"

    class Cream(models.TextChoices):
        ROUND = "round"
        STRIPE = "stripe"
        FLOWER = "flower"
        
    
    nickname = models.CharField(max_length=7, blank=False)

    email = models.OneToOneField(
        "users.User",
        on_delete=models.CASCADE,
        related_name="cakebases",
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
    
    letter = models.TextField(max_length=50, blank=True, null=True)
    
    visitor_name = models.CharField(max_length=7, blank=True, null=True)
    visitor_password = models.CharField(max_length=4, blank=True, null=True)
    

    def __str__(self) -> str:
        return f"{self.email}"


# 방문자의 케이크 꾸미기 (DecoCake)
class DecoCake(models.Model):
    
    usercake = models.ForeignKey(
        "CakeBase",
        on_delete=models.CASCADE,
        related_name="decocakes",
    )

    class Topping(models.TextChoices):
        STRAWBERRY = "strawberry"
        CHERRY = "cherry"
        SPARKLE = "sparkle"
        HEART = "heart"
        PEARL = "pearl"
        RIBBON = "ribbon"

    toppings = models.CharField(
        max_length=20,
        choices=Topping.choices,
        default=Topping.STRAWBERRY,
    )

    letter = models.TextField(
        max_length=50,
        blank=False,
        null=False,
        help_text="생일 축하 메세지를 입력하세요.",
    )

    visitor_name = models.CharField(
        max_length=7,
        blank=False,
        null=False,
        help_text= "방문자의 이름을 입력하세요.",
    )

    visitor_password = models.CharField(
        max_length=4,
        blank=False,
        null=False,
        validators=[RegexValidator(r"^\d{4}$", "비밀번호는 4자리 숫자로 이루어져야합니다.")],
        help_text="비밀번호는 4자리 숫자로 이루어져야합니다.",
    )

    # def __str__(self) -> str:
    #     return self.usercake

    def __str__(self) -> str:
        return self.visitor_name


