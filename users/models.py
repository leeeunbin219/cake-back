from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import AbstractUser
from .manager import CustomUserManager


class User(AbstractUser):
    username = None

    name = models.CharField(
        max_length=7,
        blank=False,
        validators=[MinLengthValidator(2, "이름은 2자 이상, 8자 미만 이어야합니다.")],
    )

    nickname = models.CharField(
        max_length=7,
        blank=False,
        validators=[MinLengthValidator(2, "닉네임은 2자 이상, 7자 미만 이어야합니다.")],
    )
    
    email = models.EmailField(
        blank=False,
        unique=True,
        error_messages={"unique": "이미 사용중인 이메일입니다."},
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    is_admin = models.BooleanField(default=False)

    birthday = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.nickname
