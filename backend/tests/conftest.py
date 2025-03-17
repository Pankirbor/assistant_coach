import pytest
from tests.factories import (
    UserFactory,
    WorkoutFactory,
    TrainingSegmentFactory,
    ExerciseTrainingSegmentFactory,
    SetFactory,
)


@pytest.fixture
def user():
    return UserFactory()


@pytest.fixture
def workout(user):
    return WorkoutFactory(user=user)


@pytest.fixture
def training_segment(workout):
    return TrainingSegmentFactory(workout=workout)


@pytest.fixture
def exercise_training_segment(training_segment):
    return ExerciseTrainingSegmentFactory(training_segment=training_segment)


@pytest.fixture
def approach(exercise_training_segment):
    return SetFactory(exercise=exercise_training_segment)
