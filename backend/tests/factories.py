import factory
from django.contrib.auth import get_user_model
from workout.models import (
    Workout,
    TrainingSegment,
    Exercise,
    ExerciseTrainingSegment,
    Set,
)

User = get_user_model()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker("user_name")
    password = factory.Faker("password")


class ExerciseFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Exercise

    name = factory.Faker("word")
    description = factory.Faker("sentence")


class WorkoutFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Workout

    date = factory.Faker("date")
    user = factory.SubFactory(UserFactory)


class TrainingSegmentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = TrainingSegment

    workout = factory.SubFactory(WorkoutFactory)
    timing = "00:10:00"


class ExerciseTrainingSegmentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ExerciseTrainingSegment

    training_segment = factory.SubFactory(TrainingSegmentFactory)
    exercise = factory.SubFactory(ExerciseFactory)
    target_weight = 100.0
    target_reps = 10


class SetFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Set

    exercise = factory.SubFactory(ExerciseTrainingSegmentFactory)
    actual_weight = 90.0
    actual_reps = 8
    is_last = False
