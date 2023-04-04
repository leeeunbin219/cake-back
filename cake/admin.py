from django.contrib import admin
from .models import UserCake, DecoCake


@admin.register(UserCake)
class UserCakeAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            "Cake",
            {
                "fields": (
                    "user",
                    "shape",
                    "color",
                    "image",
                    "lettering",
                ),
                "classes": ("wide",),
            },
        ),
    )

    list_display = (
        "pk",
        "user",
        "shape",
        "lettering",
        "total_visitor",
    )
    list_display_links = (
        "pk",
        "user",
        "shape",
        "lettering",
        "total_visitor",
    )


@admin.register(DecoCake)
class DecoCakeAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            "Cake",
            {
                "fields": (
                    "usercake",
                    "cream",
                    "creamcolor",
                    "letter",
                    "visitor",
                ),
                "classes": ("wide",),
            },
        ),
    )

    list_display = (
        "pk",
        "usercake",
        "letter",
        "visitor",
    )
    list_display_links = (
        "pk",
        "usercake",
        "letter",
        "visitor",
    )
