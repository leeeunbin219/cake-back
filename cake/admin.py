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
                    "cakeshape",
                    "cakecolor",
                    "cream",
                    "creamcolor",
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
        "cakeshape",
        "cream",
        "lettering",
        "total_visitor",
    )
    list_display_links = (
        "pk",
        "user",
        "cakeshape",
        "cream",
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
                    "visitor",
                    "toppings",
                    "letter",
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
        "visitor",
        "letter",
    )
