import pytest
from django.urls import reverse
from rest_framework.test import APIClient

from workout.models import ExerciseTrainingSegment, TrainingSegment, Workout


@pytest.mark.django_db
def test_update_workout_with_new_sets(
    user, workout, training_segment, exercise_training_segment
):
    print(f"WORKOUT OBJECT {workout=}")
    # Данные для обновления тренировки
    update_data = {
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
                            {"actual_weight": 95.0, "actual_reps": 9, "is_last": True},
                            {
                                "actual_weight": 100.0,
                                "actual_reps": 10,
                                "is_last": False,
                            },
                        ],
                    }
                ],
            }
        ],
    }

    client = APIClient()
    client.force_authenticate(user=user)
    url = reverse("api:workouts-detail", kwargs={"pk": workout.id})
    response = client.put(url, update_data, format="json")

    assert response.status_code == 200
    updated_workout = Workout.objects.get(id=workout.id)
    assert updated_workout.date.strftime("%Y-%m-%d") == "2023-01-02"

    updated_segment = TrainingSegment.objects.get(id=training_segment.id)
    assert updated_segment.timing == "00:15:00"

    updated_exercise_segment = ExerciseTrainingSegment.objects.get(
        id=exercise_training_segment.id
    )
    assert updated_exercise_segment.results.count() == 2

    # Ожидаемые значения сетов
    expected_sets = [
        {"actual_weight": 95.0, "actual_reps": 9, "is_last": True},
        {"actual_weight": 100.0, "actual_reps": 10, "is_last": False},
    ]

    # Проверка значений сетов в цикле
    sets = updated_exercise_segment.results.all()
    for i, expected_set in enumerate(expected_sets):
        assert sets[i].actual_weight == expected_set["actual_weight"]
        assert sets[i].actual_reps == expected_set["actual_reps"]
        assert sets[i].is_last == expected_set["is_last"]
