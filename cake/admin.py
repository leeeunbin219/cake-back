from django.contrib import admin
from .models import UserCake

@admin.register(UserCake)
class UserCakeAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            "Profile",
            {
                "fields": (
                    "user",
                    "color",
                    "image",
                    "lettering",
                ),
                "classes": ("wide",),
            },
        ),
    )

    list_display = ("user","lettering",)
    list_display_links = ("user","lettering",)