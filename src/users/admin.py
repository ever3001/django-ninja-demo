from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import Profile, User


class CustomUserAdmin(UserAdmin):
    class ProfileInline(admin.StackedInline):
        model = Profile

    model = User
    list_display = ("id", "email", "first_name", "last_name", "is_staff", "is_active")
    list_display_links = ("id", "email")
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "email",
                    "password",
                    "is_staff",
                    "is_active",
                )
            },
        ),
        (
            "Permissions",
            {
                "fields": ("groups", "user_permissions"),
                "classes": ("collapse",),
            },
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)
    inlines = (ProfileInline,)


admin.site.register(User, CustomUserAdmin)
