import pytest
from tests.factories import (
    UserFactory,
    WorkoutFactory,
    TrainingSegmentFactory,
    ExerciseTrainingSegmentFactory,
    SetFactory,
    UpdateWorkoutDataFactory,
    SetDataFactory,
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


@pytest.fixture
def update_data(workout, training_segment, exercise_training_segment):
    return {
        "id": workout.id,
        "date": "2023-01-02",
        "training_segments": [
            {
                "id": training_segment.id,
                "timing": "00:15:00",
                "exercises": [
                    {
                        "id": exercise_training_segment.id,
                        "results": [
                            SetDataFactory(),
                            SetDataFactory(
                                **{
                                    "actual_weight": 100.0,
                                    "actual_reps": 10,
                                    "is_last": True,
                                }
                            ),
                        ],
                    }
                ],
            }
        ],
    }
