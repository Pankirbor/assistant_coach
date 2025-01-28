from django.contrib import admin

from .models import CustomUser


class UserAdmin(admin.ModelAdmin):
    list_display = (
        "telegram_id",
        "username",
        "email",
        "password",
        "first_name",
        "last_name",
        "is_staff",
        "is_active",
        "date_joined",
    )
    list_filter = (
        "username",
        "email",
    )
    search_fields = (
        "username",
        "email",
    )


admin.site.register(CustomUser, UserAdmin)
