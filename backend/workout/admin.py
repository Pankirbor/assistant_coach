from django import forms
from django.contrib import admin
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.urls import reverse
from django.utils.html import format_html


from .models import (
    Exercise,
    Tag,
    Workout,
    TrainingSegment,
    Set,
    ExerciseTrainingSegment,
)


class ExerciseForm(forms.ModelForm):
    """Форма для создания и редактирования упражнений.

    Эта форма предоставляет интерфейс для ввода данных
    о упражнении, включая возможность выбора нескольких тегов
    с использованием виджета `FilteredSelectMultiple`.

    Атрибуты:
        tags (ModelMultipleChoiceField): Поле для выбора нескольких тегов,
        связанных с упражнением.

    Методы:
        class Meta: Определяет модель и используемые поля для этой формы.
    """

    # Используем FilteredSelectMultiple для поля tags
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=FilteredSelectMultiple(
            "Tags",
            is_stacked=False,
        ),
        required=False,
    )

    class Meta:
        model = Exercise
        fields = "__all__"


@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    """Админ-интерфейс для управления упражнениями.

    Позволяет отображать и редактировать запись
    об упражнении через форму `ExerciseForm`.

    Атрибуты:
        form (ModelForm): Формы, используемые в админ-интерфейсе
        для создания/редактирования упражнений.
    """

    form = ExerciseForm


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    """Админ-интерфейс для управления тегами.

    Позволяет отображать и редактировать записи о тегах,
    которые могут быть связаны с упражнениями или тренировками.

    Атрибуты:
        list_display (list): Поля, которые будут отображаться в списке тегов.
        list_display_links (list): Поля, по которым можно перейти к редактированию тегов.
    """

    list_display = ["id", "name", "slug"]
    list_display_links = ["id", "name"]


class ExerciseTrainingSegmentInline(admin.TabularInline):
    """Инлайн для управления упражнениями, связанными с сегментом тренировки.

    Позволяет добавлять и редактировать упражнения в рамках определенного
    сегмента тренировки (TrainingSegment).
    """

    model = ExerciseTrainingSegment
    extra = 1  # Количество пустых форм для добавления новых упражнений
    fields = (
        "exercise",
        "timing",
        "target_weight",
        "target_reps",
        "target_sets",
        "general_order",
        "is_done",
        "comment",
        "client_comment",
        "best_result",
    )
    readonly_fields = ("best_result",)


class TrainingSegmentInline(admin.TabularInline):
    """Инлайн для управления сегментами тренировки, связанными с тренировками.

    Позволяет добавлять и редактировать сегменты тренировки в рамках
    определенной тренировки (Workout).
    """

    model = TrainingSegment
    extra = 1  # Количество пустых форм для добавления новых сегментов тренировки
    fields = ("timing", "is_circle", "number_laps", "view_segment_link")
    readonly_fields = ["view_segment_link"]
    extra = 0

    def view_segment_link(self, obj):
        """Создает ссылку на сегмент тренировке.

        Аргументы obj (TrainingSegment): бъект тренировки, для которого создается ссылка.
        Возвращает str: HTML-код ссылки для активности в админ-интерфейсе.
        """
        url = reverse("admin:workout_trainingsegment_change", args=[obj.pk])
        return format_html(
            '<a href="{}"><img src="/static/admin/img/icon-viewlink.svg" alt="" width="20" height="20"></a>',
            url,
        )

    view_segment_link.short_description = "Упражнения"


class WorkoutForm(forms.ModelForm):
    """Форма для создания или редактирования записей о тренировках.

    Эта форма предоставляет интерфейс для ввода данных, связанных с
    тренировкой, таких как планируемая дата, пользователь и время отдыха.
    """

    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),  # Используем все доступные теги
        widget=FilteredSelectMultiple(
            "Tags",  # Отображаемое имя для виджета
            is_stacked=False,  # Установите True, если хотите вертикальное отображение
        ),
        required=False,  # Если хотите, чтобы поле было необязательным
    )

    class Meta:
        model = Workout
        fields = "__all__"


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    """Админ-интерфейс для управления тренировками (Workout).

    Позволяет отображать и управлять записями о тренировках,
    включая их сегменты тренировки.
    """

    form = WorkoutForm
    inlines = [TrainingSegmentInline]


@admin.register(TrainingSegment)
class TrainingSegmentAdmin(admin.ModelAdmin):
    """Админ-интерфейс для управления сегментами тренировок.

    Позволяет отображать и редактировать записи о сегментах тренировок,
    которые связаны с определенной тренировкой (Workout).
    """

    list_display = [
        "workout",
        "timing",
        "is_circle",
        "number_laps",
    ]
    inlines = [ExerciseTrainingSegmentInline]


@admin.register(Set)
class SetAdmin(admin.ModelAdmin):
    """Админ-интерфейс для управления записями об упражнениях.

    Позволяет отображать и редактировать записи о целевых и фактических
    значениях для повторений и веса для каждого упражнения в сегменте.
    """

    list_display = [
        "excercise",
        "target_weight",
        "terget_reps",
        "actual_weight",
        "actual_reps",
        "comment",
        "is_last",
    ]


@admin.register(ExerciseTrainingSegment)
class ExerciseTrainingSegmentAdmin(admin.ModelAdmin):
    """Админ-интерфейс для управления записями об упражнениях в
    сегментах тренировок.

    Позволяет отображать и редактировать информацию о планируемых
    или выполненных упражнениях в рамках конкретного сегмента тренировки.
    """

    list_display = [
        "exercise",
        "training_segment",
        "timing",
        "target_weight",
        "target_reps",
        "target_sets",
        "general_order",
        "is_done",
        "comment",
        "client_comment",
        "best_result",
    ]
