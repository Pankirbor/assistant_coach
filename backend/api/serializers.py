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


class SetSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Set.

    Этот сериализатор используется для представления наборов,
    создаваемых во время тренировки, включая целевой вес, фактический вес
    и количество повторений, а также комментарии к набору.
    """

    target_weight = serializers.ReadOnlyField(source="excercise.target_weight")
    terget_reps = serializers.ReadOnlyField(source="excercise.target_reps")

    class Meta:
        model = Set
        fields = (
            "target_weight",
            "terget_reps",
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

    exercise_id = serializers.ReadOnlyField(source="exercise.id")
    name = serializers.ReadOnlyField(source="exercise.name")
    video_link = serializers.ReadOnlyField(source="exercise.video_link")
    results = SetSerializer(many=True)

    class Meta:
        model = ExerciseTrainingSegment
        fields = (
            "id",
            "exercise_id",
            "name",
            "video_link",
            "timing",
            "target_weight",
            "target_reps",
            "target_sets",
            "general_order",
            "is_done",
            "comment",
            "client_comment",
            "best_result",
            "results",
        )
        read_only_fields = (
            "id",
            "exercise_id",
            "name",
            "video_link",
            "timing",
            "target_weight",
            "target_reps",
            "target_sets",
            "general_order",
            "is_done",
            "comment",
            "best_result",
        )

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
        results_for_save = [Set(excercise_id=instance.id, **item) for item in results]
        Set.objects.bulk_create(results_for_save)
        return super().update(instance, validated_data)


class TrainingSegmentSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели TrainingSegment.

    Этот сериализатор предназначен для представления сегментов тренировок,
    включая время, тип сегмента и запланированные упражнения.
    """

    exercises = ExerciseTrainingSegmentSerializer(
        many=True, source="scheduled_exercises"
    )

    class Meta:
        model = TrainingSegment
        fields = ("timing", "is_circle", "number_laps", "exercises")


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
        fields = ("id", "date", "client", "tags", "timing", "training_segments")


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
            "actual_weight",
            "actual_reps",
            "comment",
            "is_last",
        )
