from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from .models import CustomUser
from workout.models import Workout


class WorkoutInline(admin.TabularInline):
    """Инлайн для управления записями о тренировках, связанными с пользователем.

    Позволяет отображать и редактировать тренировки в админке на странице пользователя.

    Атрибуты:
        model (Model): Модель, с которой связан данный инлайн (Workout).
        fields (list): Список полей, которые будут отображены в инлайне.
        readonly_fields (list): Поля, которые будут доступны только для чтения.
        extra (int): Количество дополнительных форм для добавления новых записей. Присвоено 0.
    """

    model = Workout
    fields = [
        "view_workout_link",
    ]
    readonly_fields = ["view_workout_link"]
    extra = 0

    def view_workout_link(self, obj):
        """Создает ссылку для редактирования записи о тренировке.

        Аргументы obj (Workout): бъект тренировки, для которого создается ссылка.
        Возвращает str: HTML-код ссылки для активности в админ-интерфейсе.
        """
        url = reverse("admin:workout_workout_change", args=[obj.pk])
        return format_html('<a href="{}">View Workout for {}</a>', url, obj.date)

    view_workout_link.short_description = "Workout"


class UserAdmin(admin.ModelAdmin):
    """Админ-интерфейс для управления пользователями.

    Позволяет отображать и редактировать информацию о пользователе, включая его тренировки.

    Атрибуты:
        list_display (tuple): Поля, которые будут отображаться в списке пользователей.
        inlines (list): Список инлайнов, которые будут отображаться на странице пользователя.
        list_filter (tuple): Поля, по которым можно фильтровать пользователей в админке.
        search_fields (tuple): Поля, по которым можно искать пользователей.
        list_display_links (list): Поля, по которым можно перейти к редактированию пользователя.
    """

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
    inlines = [WorkoutInline]
    list_filter = (
        "username",
        "email",
    )
    search_fields = (
        "username",
        "email",
    )
    list_display_links = ["username"]


admin.site.register(CustomUser, UserAdmin)
