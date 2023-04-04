from django.contrib import admin
from .models import Visitor


@admin.register(Visitor)
class VisitorAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            "Visitor",
            {
                "fields": (
                    "nickname",
                    "password",
                ),
                "classes": ("wide",),
            },
        ),
    )

    list_display = (
        "nickname",
    )
    list_display_links = (
        "nickname",
    )
