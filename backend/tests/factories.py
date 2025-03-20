from datetime import datetime
from factory.django import DjangoModelFactory
from factory import DictFactory, List, Faker, LazyAttribute, SelfAttribute, SubFactory
from django.contrib.auth import get_user_model
from workout.models import (
    Workout,
    TrainingSegment,
    Exercise,
    ExerciseTrainingSegment,
    Set,
)

User = get_user_model()


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = Faker("user_name")
    password = Faker("password")


class ExerciseFactory(DjangoModelFactory):
    class Meta:
        model = Exercise

    name = Faker("word")
    description = Faker("sentence")


class WorkoutFactory(DjangoModelFactory):
    class Meta:
        model = Workout

    date = Faker("date")
    user = SubFactory(UserFactory)


class TrainingSegmentFactory(DjangoModelFactory):
    class Meta:
        model = TrainingSegment

    workout = SubFactory(WorkoutFactory)
    timing = "00:10:00"


class ExerciseTrainingSegmentFactory(DjangoModelFactory):
    class Meta:
        model = ExerciseTrainingSegment

    training_segment = SubFactory(TrainingSegmentFactory)
    exercise = SubFactory(ExerciseFactory)
    target_weight = 100.0
    target_reps = 10


class SetFactory(DjangoModelFactory):
    class Meta:
        model = Set

    exercise = SubFactory(ExerciseTrainingSegmentFactory)
    actual_weight = 90.0
    actual_reps = 8
    is_last = False


class SetDataFactory(DictFactory):
    actual_weight = 95.0
    actual_reps = 9
    is_last = False


class ExerciseDataFactory(DictFactory):
    id = LazyAttribute(lambda o: o.exercise_training_segment.id)
    results = List(
        [
            SetDataFactory(),
            SetDataFactory(actual_weight=100, actual_reps=10, is_last=True),
        ]
    )

    @classmethod
    def _adjust_results(cls, results_count, **kwargs):
        """
        Метод для настройки количества объектов в results.
        """
        if results_count is not None:
            return List([SetDataFactory(**kwargs) for _ in range(results_count)])

        return List(
            [
                SetDataFactory(),
                SetDataFactory(actual_weight=100, actual_reps=10, is_last=True),
            ]
        )

    @classmethod
    def create(cls, results_count=None, **kwargs):
        kwargs["results"] = cls._adjust_results(results_count, **kwargs)
        return super().create(**kwargs)


class TrainingSegmentDataFactory(DictFactory):
    id = LazyAttribute(lambda o: o.training_segment.id)
    timing = "00:15:00"
    scheduled_exercises = List(
        [
            SubFactory(ExerciseDataFactory),
            SubFactory(ExerciseDataFactory),
        ]
    )


class UpdateWorkoutDataFactory(DictFactory):
    id = LazyAttribute(lambda o: o.workout.id)
    date = LazyAttribute(lambda o: datetime.now().strftime("%Y-%m-%d"))
    training_segments = List(
        [
            SubFactory(
                TrainingSegmentDataFactory,
            )
        ]
    )
