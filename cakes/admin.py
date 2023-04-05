from django.contrib import admin
from .models import CakeBase, DecoCake


@admin.register(CakeBase)
class CakeBaseAdmin(admin.ModelAdmin):
    fieldsets = (
        (
                "UserCake",
                {
                    "fields": (
                        "email",
                        "nickname",
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
        "nickname",
        "cakeshape",
        "cream",
        "lettering",
    )

    list_display_links = (
        "pk",
        "nickname",
        "cakeshape",
        "cream",
        "lettering",
    )
    
    list_filter = ("nickname","cakeshape","cream")
    


@admin.register(DecoCake)
class DecoAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            "Decorate",
            {
                "fields": (
                    "usercake",
                    "toppings",
                    "visitor_name",
                    "visitor_password",
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
        "visitor_name",
    )

    list_display_links = (
        "pk",
        "usercake",
        "letter",
        "visitor_name",
    )
    
    list_filter = ("usercake","visitor_name")
