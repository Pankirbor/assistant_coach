from django.db import transaction
from django.shortcuts import get_object_or_404
from rest_framework import serializers

from workout.models import (
    Tag,
    Exercise,
    TrainingSegment,
    ExerciseTrainingSegment,
    Workout,
    Set,
)
from users.models import CustomUser
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("api")
logger.debug("Проверка StreamHandler")


class UserSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели CustomUser.

    Этот сериализатор предназначен для представления данных пользователя,
    включая его идентификатор, идентификатор Telegram, имя пользователя,
    имя, фамилию и адрес электронной почты.
    """

    class Meta:
        model = CustomUser
        fields = [
            "id",
            "telegram_id",
            "username",
            "first_name",
            "last_name",
            "email",
        ]


class TagSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Tag.

    Этот сериализатор позволяет представлять теги, включая их
    идентификатор, имя и слаг.
    """

    class Meta:
        model = Tag
        fields = ("id", "name", "slug")


class ExerciseSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Exercise.

    Этот сериализатор используется для представления данных
    о упражнениях, включая их идентификатор, название, описание
    и ссылку на видео.
    """

    class Meta:
        model = Exercise
        fields = ("id", "name", "description", "video_link")


class SetCreateSerializer(serializers.ModelSerializer):
    """
    Сериализатор для создания экземпляров Set.

    Этот сериализатор используется для представления данных,
    необходимых для создания нового набора, включая фактический вес,
    количество повторений, комментарии и информацию о том,
    является ли набор последним.
    """

    class Meta:
        model = Set
        fields = (
            "target_reps",
            "target_weight",
            "actual_weight",
            "actual_reps",
            "comment",
            "is_last",
        )


class SetSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Set.

    Этот сериализатор используется для представления наборов,
    создаваемых во время тренировки, включая целевой вес, фактический вес
    и количество повторений, а также комментарии к набору.
    """

    target_weight = serializers.ReadOnlyField(source="exercise.target_weight")
    target_reps = serializers.ReadOnlyField(source="exercise.target_reps")

    class Meta:
        model = Set
        fields = (
            "target_weight",
            "target_reps",
            "actual_weight",
            "actual_reps",
            "comment",
            "is_last",
        )


class ExerciseTrainingSegmentSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели ExerciseTrainingSegment.

    Этот сериализатор предназначен для представления упражнений в
    сегментах тренировки, включая ID упражнения, его название,
    ссылку на видео и результаты наборов.
    """

    # id = serializers.IntegerField()
    # exercise = serializers.IntegerField(required=False)
    # training_segment = serializers.IntegerField(required=False)
    exercise_id = serializers.ReadOnlyField(source="exercise.id")
    name = serializers.ReadOnlyField(source="exercise.name")
    video_link = serializers.ReadOnlyField(source="exercise.video_link")
    results = SetCreateSerializer(many=True)

    class Meta:
        model = ExerciseTrainingSegment
        fields = "__all__"  # (
        #     "id",
        #     "exercise_id",
        #     "name",
        #     "video_link",
        #     "timing",
        #     "target_weight",
        #     "target_reps",
        #     "target_sets",
        #     "general_order",
        #     "is_done",
        #     "comment",
        #     "client_comment",
        #     "best_result",
        #     "results",
        # )

    def create(self, validated_data):
        """
        Создает или обновляет запись ExerciseTrainingSegment.
        """
        exercise = validated_data.get("exercise")
        training_segment = validated_data.get("training_segment")

        # Проверяем, существует ли запись
        instance, created = ExerciseTrainingSegment.objects.get_or_create(
            exercise=exercise,
            training_segment=training_segment,
            defaults=validated_data,
        )

        if not created:
            # Если запись существует, обновляем её
            for attr, value in validated_data.items():
                setattr(instance, attr, value)
            instance.save()

        return instance

    def update(self, instance, validated_data):
        """
        Обновляет существующий экземпляр ExerciseTrainingSegment.

        При обновлении извлекаются результаты наборов из валидированных
        данных, создаются новые экземпляры Set и сохраняются в базе данных.

        Args:
        instance: Экземпляр ExerciseTrainingSegment, который нужно обновить.
            validated_data: Валидированные данные для обновления.

        Returns:
            Обновленный экземпляр ExerciseTrainingSegment.
        """
        results = validated_data.pop("results")
        results_for_save = [Set(exercise=instance, **item) for item in results]
        Set.objects.bulk_create(results_for_save)
        return super().update(instance, validated_data)


class ExerciseTrainingSegmentCreateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    exercise = ExerciseSerializer(
        read_only=True
    )  # serializers.PrimaryKeyRelatedField(queryset=Exercise.objects.all())
    training_segment = serializers.PrimaryKeyRelatedField(
        queryset=TrainingSegment.objects.all()
    )
    results = SetCreateSerializer(many=True)

    class Meta:
        model = ExerciseTrainingSegment
        fields = "__all__"

    def create(self, validated_data):
        """
        Создает или обновляет запись ExerciseTrainingSegment.
        """
        exercise = validated_data.get("exercise")
        training_segment = validated_data.get("training_segment")

        # Проверяем, существует ли запись
        instance, created = ExerciseTrainingSegment.objects.get_or_create(
            exercise=exercise,
            training_segment=training_segment,
            defaults=validated_data,
        )

        if not created:
            # Если запись существует, обновляем её
            for attr, value in validated_data.items():
                setattr(instance, attr, value)
            instance.save()

        return instance

    def update(self, instance, validated_data):
        """
        Обновляет существующий экземпляр ExerciseTrainingSegment.

        При обновлении извлекаются результаты наборов из валидированных
        данных, создаются новые экземпляры Set и сохраняются в базе данных.

        Args:
        instance: Экземпляр ExerciseTrainingSegment, который нужно обновить.
            validated_data: Валидированные данные для обновления.

        Returns:
            Обновленный экземпляр ExerciseTrainingSegment.
        """
        logger.debug(f"Начало обновления упражнения {instance.id}")

        results = validated_data.pop("results")  # Удаляем старые подходы
        Set.objects.filter(exercise=instance).delete()
        logger.debug(f"Удалены старые подходы для упражнения {instance.id}")

        # Создаем новые подходы
        results_for_save = [Set(exercise=instance, **item) for item in results]

        created_sets = Set.objects.bulk_create(results_for_save)
        logger.debug(
            f"Созданы новые подходы для упражнения {instance.id}: {created_sets}"
        )

        # Если хотя бы один подход является последним, обновляем лучший результат
        if any(result.is_last for result in created_sets):
            logger.debug(
                f"Найден последний подход, попытка вызвать метод update_best_result"
            )
            validated_data.pop("best_result")
            instance.update_best_result()

        return super().update(instance, validated_data)


class TrainingSegmentSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели TrainingSegment.

    Этот сериализатор предназначен для представления сегментов тренировок,
    включая время, тип сегмента и запланированные упражнения.
    """

    id = serializers.IntegerField()
    workout = serializers.PrimaryKeyRelatedField(queryset=Workout.objects.all())
    exercises = ExerciseTrainingSegmentCreateSerializer(
        many=True,
        source="scheduled_exercises",
    )

    class Meta:
        model = TrainingSegment
        fields = (
            "__all__"  # ("workout", "timing", "is_circle", "number_laps", "exercises")
        )


class WorkoutSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Workout.

    Этот сериализатор используется для представления информации о тренировках,
    включая дату, клиента, теги и сегменты тренировок.
    """

    tags = TagSerializer(read_only=True, many=True)
    training_segments = TrainingSegmentSerializer(read_only=True, many=True)
    client = UserSerializer(read_only=True, source="user")

    class Meta:
        model = Workout
        fields = "__all__"


class WorkoutCreateSerializer(serializers.ModelSerializer):
    """
    Сериализатор для создания или обновления объектов модели Workout.
    """

    tags = TagSerializer(many=True, read_only=True)
    training_segments = TrainingSegmentSerializer(many=True)
    client = UserSerializer(read_only=True)

    class Meta:
        model = Workout
        fields = ["id", "date", "client", "tags", "timing", "training_segments"]

    def update(self, instance, validated_data):
        """
        Обновляет существующую тренировку, включая сегменты, упражнения и подходы.

        Args:
            instance: Экземпляр Workout, который нужно обновить.
            validated_data: Валидированные данные для обновления.

        Returns:
            Обновленный экземпляр Workout.

        Raises:
            serializers.ValidationError: Если произошла ошибка при обновлении.
        """
        logger.debug(f"Начало обновления тренировки {instance.id}")

        try:
            with transaction.atomic():
                # Удаляем client и tags из validated_data, так как они не обновляются
                validated_data.pop("client", None)
                validated_data.pop("tags", None)

                # Обновляем основные поля тренировки
                instance.date = validated_data.get("date", instance.date)
                instance.timing = validated_data.get("timing", instance.timing)
                instance.save()

                # Обрабатываем тренировочные сегменты
                training_segments_data = validated_data.pop("training_segments", [])
                logger.debug(
                    f"Данные тренировочных сегментов: {training_segments_data=}"
                )

                for segment_data in training_segments_data:
                    segment_id = segment_data.get("id")
                    logger.debug(f"Полученный {segment_id=}")
                    if segment_id:
                        segment = get_object_or_404(
                            TrainingSegment, id=segment_id, workout=instance
                        )
                        logger.debug(f"Полученный {segment_id=} найден {segment=}")
                    else:
                        logger.debug(f"Необходимый segment_id {segment_id=} не найден!")
                        continue

                    segment.timing = segment_data.get("timing", segment.timing)
                    segment.is_circle = segment_data.get("is_circle", segment.is_circle)
                    segment.number_laps = segment_data.get(
                        "number_laps", segment.number_laps
                    )
                    segment.save()

                    logger.debug(f"Обновленный {segment=}")

                    # Обрабатываем упражнения в сегменте
                    exercises_data = segment_data.get("scheduled_exercises", [])
                    logger.debug(f"Данные упражнений: {exercises_data}")

                    for exercise_data in exercises_data:
                        exercise_id = exercise_data.get("id")
                        logger.debug(f"Полученный объект {exercise_id=}")
                        if exercise_id:
                            exercise = get_object_or_404(
                                ExerciseTrainingSegment,
                                id=exercise_id,
                                training_segment=segment,
                            )
                            logger.debug(
                                f"Полученный объект {exercise_id=} найден {exercise=}"
                            )
                        else:
                            logger.debug(
                                f"Необходимый exercise_id {exercise_id=} не найден!"
                            )
                            continue

                        for key, value in exercise_data.items():
                            if key != "results":
                                setattr(exercise, key, value)

                        exercise.save()

                        # Обрабатываем подходы (Set)
                        results_data = exercise_data.get("results", [])
                        logger.debug(f"Данные подходов: {results_data}")

                        # Удаляем старые подходы
                        Set.objects.filter(exercise=exercise).delete()

                        # Создаем новые подходы
                        results_for_save = [
                            Set(exercise=exercise, **item) for item in results_data
                        ]
                        created_sets = Set.objects.bulk_create(results_for_save)

                        if any(result.is_last for result in created_sets):
                            exercise.update_best_result()

                logger.debug(f"Тренировка {instance.id} успешно обновлена")
                return instance

        except Exception as e:
            logger.error(f"Ошибка при обновлении тренировки {instance.id}: {e}")
            raise serializers.ValidationError(f"Ошибка при обновлении тренировки: {e}")

    # def update(self, instance, validated_data):
    #     logger.debug(f"Validated data: {validated_data}")
    #     try:

    #         with transaction.atomic():
    #             # Удаляем client и tags из validated_data, чтобы они не обновлялись
    #             validated_data.pop("client", None)
    #             validated_data.pop("tags", None)

    #             training_segments = validated_data.get("training_segments", [])
    #             logger.debug(f"Training segments: {training_segments}")
    #             exercises_to_update = []
    #             for segment in training_segments:
    #                 exercises_to_update.extend(segment.pop("scheduled_exercises", []))

    #             for ex in exercises_to_update:
    #                 ex_id = ex.get("id")
    #                 if not ex_id:
    #                     logger.warning(f"Отсутствует ID для упражнения: {ex}")
    #                     continue  # Пропускаем упражнение без ID
    #                 ex_obj = get_object_or_404(ExerciseTrainingSegment, id=ex.get("id"))
    #                 results = ex.get("results", [])
    #                 logger.debug(
    #                     f"Updating results for exercise {ex_obj.id}: {results}"
    #                 )
    #                 Set.objects.filter(excercise=ex_obj).delete()
    #                 results_for_save = [
    #                     Set(excercise=ex_obj, **item) for item in results
    #                 ]
    #                 Set.objects.bulk_create(results_for_save)

    #             return super().update(instance, validated_data)
    #     except Exception as e:
    #         logger.error(f"Ошибка при обновлении тренировки: {e}")
    #         raise serializers.ValidationError(f"Ошибка при обновлении тренировки: {e}")

    def to_representation(self, instance):
        serializer = WorkoutSerializer(
            instance, context={"request": self.context.get("request")}
        )
        return serializer.data
