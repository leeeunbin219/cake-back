from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            "Profile",
            {
                "fields": (
                    "name",
                    "nickname",
                    "email",
                    "birthday",
                    "is_admin",
                    # "cake",
                ),
                "classes": ("wide",),
            },
        ),
        (
            "Permissions",
            {
                "fields": ("is_active", "is_staff", "is_superuser", "user_permissions"),
                "classes": ("collapse",),
            },
        ),
        (
            "Important dates",
            {
                "fields": ("last_login", "date_joined"),
                "classes": ("collapse",),
            },
        ),
    )

    list_display = ("pk","name", "nickname", "email", "birthday", "is_admin")
    list_display_links = ("pk","name", "nickname", "email")
