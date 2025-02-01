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
    class Meta:
        model = Tag
        fields = ("id", "name", "slug")


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ("id", "name", "description", "video_link")


class SetSerializer(serializers.ModelSerializer):
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
        results = validated_data.pop("results")
        results_for_save = [Set(excercise_id=instance.id, **item) for item in results]
        Set.objects.bulk_create(results_for_save)
        return super().update(instance, validated_data)


class TrainingSegmentSerializer(serializers.ModelSerializer):
    exercises = ExerciseTrainingSegmentSerializer(
        many=True, source="scheduled_exercises"
    )

    class Meta:
        model = TrainingSegment
        fields = ("timing", "is_circle", "number_laps", "exercises")


class WorkoutSerializer(serializers.ModelSerializer):
    tags = TagSerializer(read_only=True, many=True)
    training_segments = TrainingSegmentSerializer(read_only=True, many=True)
    client = UserSerializer(read_only=True, source="user")

    class Meta:
        model = Workout
        fields = ("id", "date", "client", "tags", "timing", "training_segments")


class SetCreateSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField()
    # exercise = serializers.PrimaryKeyRelatedField(
    #     queryset=ExerciseTrainingSegment.objects.all()
    # )

    class Meta:
        model = Set
        fields = (
            "actual_weight",
            "actual_reps",
            "comment",
            "is_last",
        )
