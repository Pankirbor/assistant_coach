from rest_framework import serializers

from workout.models import (
    Tag,
    Exercise,
    TrainingSegment,
    ExerciseTrainingSegment,
    Workout,
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


class ExerciseTrainingSegmentSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField(source="exercise.id")
    name = serializers.ReadOnlyField(source="exercise.name")
    video_link = serializers.ReadOnlyField(source="exercise.video_link")

    class Meta:
        model = ExerciseTrainingSegment
        fields = (
            "id",
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
        )


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
    client = UserSerializer(read_only=True)

    class Meta:
        model = Workout
        fields = ("id", "date", "client", "tags", "timing", "training_segments")
