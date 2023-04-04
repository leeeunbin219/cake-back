from django.db import models
from django.core.validators import RegexValidator


class Visitor(models.Model):
    nickname = models.CharField(max_length=7)
    password = models.CharField(
        max_length=4,
        blank=False,
        null=False,
        validators=[RegexValidator(r"^\d{4}$", "비밀번호는 4자리 숫자로 이루어져야합니다.")],
        help_text="비밀번호는 4자리 숫자로 이루어져야합니다.",
    )

    def __str__(self):
        return self.nickname
