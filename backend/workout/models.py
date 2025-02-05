from decimal import Decimal
from django.db import models

from users.models import CustomUser


class Exercise(models.Model):
    """
    Модель упражнения.

    Содержит информацию о упражнении, включая его название,
    описание, ссылку на видео и связанные теги.
    """

    name = models.CharField("Название", max_length=200)
    description = models.TextField("Описание", blank=True, null=True)
    video_link = models.CharField(
        "Видеоинструкция", blank=True, null=True, max_length=255
    )
    tags = models.ManyToManyField(
        "Tag",
        through="TagExercise",
        verbose_name="Тэг упражнения",
        related_name="exercises",
    )

    class Meta:
        verbose_name = "Упражнение"
        verbose_name_plural = "Упражнения"

    def __str__(self):
        return f"Упражнение {self.name}"


class Tag(models.Model):
    """
    Модель тега.

    Содержит информацию о тегах, включая название и слаг,
    а также обеспечивает уникальность сочетания
    имени и слага.
    """

    name = models.CharField("Название", max_length=150)
    slug = models.SlugField(
        "слаг Тега",
        unique=True,
        max_length=50,
        db_index=True,
    )

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"
        constraints = [
            models.UniqueConstraint(fields=["name", "slug"], name="unique_tag"),
        ]

    def __str__(self):
        return self.name


class TagExercise(models.Model):
    """
    Связующая модель между упражнениями и тегами.

    Эта модель позволяет реализовать связь многие-ко-многим
    между моделями Exercise и Tag.
    """

    tag = models.ForeignKey(
        Tag,
        on_delete=models.CASCADE,
        verbose_name="Тег",
    )
    exercise = models.ForeignKey(
        Exercise,
        on_delete=models.CASCADE,
        verbose_name="Упражнение",
    )

    class Meta:
        verbose_name = "Упражнение и тэг"
        verbose_name_plural = "Упражнения и тэги"
        constraints = [
            models.UniqueConstraint(
                fields=["tag", "exercise"],
                name="unique_exercise_tag",
            ),
        ]

    def __str__(self):
        return f"{self.exercise} с тегом {self.tag}"


class Workout(models.Model):
    """
    Модель тренировки.

    Содержит информацию о тренировках, включая планируемую дату,
    клиента, таймер и связанные с тренировкой теги.
    """

    date = models.DateField("Дата тренировки", db_index=True)
    user = models.ForeignKey(
        CustomUser,
        verbose_name="Клиент",
        related_name="workouts",
        on_delete=models.SET_NULL,
        null=True,
    )
    timing = models.CharField(
        "Таймер",
        max_length=150,
        default="",
        blank=True,
        null=True,
    )
    tags = models.ManyToManyField(
        Tag,
        through="TagWorkout",
        verbose_name="Тэги тренировки",
        related_name="workouts",
    )

    class Meta:
        verbose_name = "Тренировка"
        verbose_name_plural = "Тренировки"

    def __str__(self):
        """Метод строкового представления модели"""

        return f"Тренировка для {self.user.username} на {self.date}"


class TagWorkout(models.Model):
    """
    Связующая модель между тренировками и тегами.

    Эта модель позволяет реализовать связь многие-ко-многим
    между моделями Workout и Tag.
    """

    tag = models.ForeignKey(
        Tag,
        on_delete=models.CASCADE,
        verbose_name="Тег",
    )
    workout = models.ForeignKey(
        Workout,
        on_delete=models.CASCADE,
        verbose_name="Тренировка",
    )

    class Meta:
        verbose_name = "Тренировка и тэг"
        verbose_name_plural = "Тренировки и тэги"
        constraints = [
            models.UniqueConstraint(
                fields=["tag", "workout"],
                name="unique_workout_tag",
            ),
        ]

    def __str__(self):
        return f"{self.workout} с тегом {self.tag}"


class TrainingSegment(models.Model):
    """
    Модель тренировочного блока.

    Содержит информацию о тренировочном блоке, включая
    связанную тренировку, таймер и список упражнений в блоке.
    """

    workout = models.ForeignKey(
        Workout,
        related_name="training_segments",
        verbose_name="Тренировка",
        on_delete=models.CASCADE,
    )
    timing = models.CharField(
        "Таймер",
        max_length=150,
        default="",
        blank=True,
        null=True,
    )
    is_circle = models.BooleanField("Круговая", default=False)
    number_laps = models.IntegerField("Количество кругов", default=1)
    exercises = models.ManyToManyField(
        Exercise,
        through="ExerciseTrainingSegment",
        verbose_name="Упражнения в блоке",
        related_name="training_segment",
    )

    class Meta:
        verbose_name = "Тренировочный блок"
        verbose_name_plural = "Тренировочные блоки"

    def __str__(self):
        return f"Тренировочный блок для {self.workout}"


class ExerciseTrainingSegment(models.Model):
    """
    Модель упражнения сегмента тренировки с упражнениями.

    Содержит информацию об упражнениях, запланированных в блоке тренировки,
    включая время, вес и количество повторений, а также статус выполнения.
    """

    exercise = models.ForeignKey(
        Exercise,
        related_name="present_in_workouts",
        verbose_name="Упражнение",
        on_delete=models.CASCADE,
    )
    training_segment = models.ForeignKey(
        TrainingSegment,
        related_name="scheduled_exercises",
        verbose_name="Блок упражнений",
        on_delete=models.CASCADE,
    )
    timing = models.CharField(
        "Таймер",
        max_length=150,
        default="",
        blank=True,
        null=True,
    )
    target_weight = models.DecimalField(
        "Планируемый вес", max_digits=5, decimal_places=2, default=Decimal("0.00")
    )
    target_reps = models.IntegerField(
        "Планируемое кол-во повторений",
        blank=True,
        null=True,
    )
    target_sets = models.IntegerField(
        "Планируемое кол-во подходов",
        blank=True,
        null=True,
    )
    general_order = models.IntegerField(
        "Порядковый номер",
        blank=True,
        null=True,
    )
    is_done = models.BooleanField("Статус выполнения", default=False)
    comment = models.TextField("Комментарий тренера", blank=True, null=True)
    client_comment = models.TextField("Комментарий клиента", blank=True, null=True)
    best_result = models.DecimalField(
        "Лучший результат", max_digits=5, decimal_places=2, default=Decimal("0.00")
    )

    class Meta:
        verbose_name = "Упражнение и блок"
        verbose_name_plural = "Упражнения и блоки"
        constraints = [
            models.UniqueConstraint(
                fields=["training_segment", "exercise"],
                name="unique_exercise_training_segment",
            ),
        ]

    def __str__(self):
        """
        Возвращает строковое представление объекта.

        Returns:
            str: Форматированное строковое представление объекта
            с указанием упражнения и блока тренировки.
        """
        return f"Заданное {self.exercise} для блока {self.training_segment}"

    def update_best_result(self):
        """
        Обновляет лучший результат выполнения упражнения.

        Устанавливает статус выполнения как завершенный,
        вычисляет лучший результат среди всех результатов
        тренировочного сегмента и сохраняет его.
        """
        self.is_done = True
        best_result = self.results.aggregate(models.Max("actual_weight"))[
            "actual_weight__max"
        ]
        self.best_result = best_result
        self.save()


class Set(models.Model):
    """
    Модель подхода в тренировке.

    Содержит информацию о конкретном подходе к упражнению,
    включая фактический вес и количество повторений,
    а также комментарии и статус последнего подхода.
    """

    excercise = models.ForeignKey(
        ExerciseTrainingSegment, on_delete=models.CASCADE, related_name="results"
    )
    target_weight = models.DecimalField(
        "Планируемый вес",
        max_digits=5,
        decimal_places=2,
        default=Decimal("0.00"),
        blank=True,
        null=True,
    )
    terget_reps = models.IntegerField(
        "Планируемое кол-во повторений",
        blank=True,
        null=True,
    )
    actual_weight = models.DecimalField(
        "Фактический вес",
        max_digits=5,
        decimal_places=2,
        default=Decimal("0.00"),
    )
    actual_reps = models.IntegerField(
        "Фактическое кол-во повторений",
        blank=True,
    )
    comment = models.TextField("Комментарий", blank=True, null=True)
    is_last = models.BooleanField("Заключетельный подход", default=False)

    class Meta:
        verbose_name = "Подход"
        verbose_name_plural = "Подходы"

    def __str__(self):
        """
        Возвращает строковое представление объекта.

        Returns:
            str: Форматированное строковое представление объекта
            с указанием названия упражнения.
        """
        return f"Подход для {self.excercise.exercise.name}"

    def save(self, *args, **kwargs):
        """
        Сохраняет объект подхода в базе данных.

        После сохранения проверяет, является ли подход последним,
        и если да, то обновляет лучший результат в соответствующем
        тренировочном сегменте.

        Args:
            *args: Позиционные аргументы для метода save.
            **kwargs: Именованные аргументы для метода save.
        """
        super().save(*args, **kwargs)
        if self.is_last:
            self.excercise.update_best_result()
