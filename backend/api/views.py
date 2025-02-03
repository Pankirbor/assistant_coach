from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema_view, extend_schema

from .serializers import (
    UserSerializer,
    WorkoutSerializer,
    SetSerializer,
    SetCreateSerializer,
    ExerciseTrainingSegmentSerializer,
)

from . import description_points
from workout.models import Set, Workout, ExerciseTrainingSegment
from users.models import CustomUser


@extend_schema_view(
    list=extend_schema(**description_points.user_list_endpoint),
    retrieve=extend_schema(**description_points.user_detail_endpoint),
    create=extend_schema(**description_points.user_create_endpoint),
    update=extend_schema(**description_points.user_put_endpoint),
    destroy=extend_schema(**description_points.user_delete_endpoint),
)
class UserViewSet(viewsets.ModelViewSet):
    """
    Обеспечивает представление пользователя для выполнения CRUD операций.

    Этот класс предоставляет все стандартные операции
    для управления пользователями, включая:
    - получение списка пользователей
    - получение деталей конкретного пользователя
    - создание нового пользователя
    - обновление существующего пользователя
    - удаление пользователя
    """

    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


@extend_schema_view(
    list=extend_schema(**description_points.workouts_list_endpoint),
    retrieve=extend_schema(**description_points.workouts_detail_endpoint),
    create=extend_schema(**description_points.workouts_create_endpoint),
    update=extend_schema(**description_points.workouts_update_endpoint),
    destroy=extend_schema(**description_points.workouts_delete_endpoint),
    partial_update=extend_schema(**description_points.workouts_patch_endpoint),
)
class WorkoutViewSet(viewsets.ModelViewSet):
    """
    Обеспечивает представление тренировок для выполнения CRUD операций.

    Этот класс позволяет пользователям (тренерам или клиентам)
    управлять тренировками, включая:
    - создание новых тренировок
    - получение информации о конкретной тренировке
    - обновление существующих тренировок
    - удаление тренировок
    """

    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer

    @extend_schema(summary="Получение запланированой тренировки на сегодня.")
    @action(
        methods=["get"],
        detail=False,
        url_path="next_workout",
    )
    def next_workout(self, request):
        """
        Возвращает последнюю запланированную тренировку пользователя.

        Этот метод обрабатывает GET-запрос и возвращает
        последнюю запланированную тренировку.
        """
        user = request.user
        next_workout = Workout.objects.filter(user=user).last()
        serializer = self.get_serializer(next_workout)
        return Response(serializer.data)


@extend_schema_view(
    list=extend_schema(**description_points.exercise_training_segment_list_endpoint),
    retrieve=extend_schema(
        **description_points.exercise_training_segment_detail_endpoint
    ),
    create=extend_schema(
        **description_points.exercise_training_segment_create_endpoint
    ),
    update=extend_schema(
        **description_points.exercise_training_segment_update_endpoint
    ),
    destroy=extend_schema(
        **description_points.exercise_training_segment_delete_endpoint
    ),
    partial_update=extend_schema(
        **description_points.exercise_training_segment_patch_endpoint
    ),
)
class ExerciseTrainingSegmentViewSet(viewsets.ModelViewSet):
    """
    Обеспечивает представление упражнений в контексте тренировок для выполнения CRUD операций.

    Этот класс позволяет управлять упражнениями тренировок, включая:
    - создание новых упражнений
    - получение информации о конкретном упражнении
    - обновление существующих упражнений
    - удаление упражнений
    """

    queryset = ExerciseTrainingSegment.objects.all()
    serializer_class = ExerciseTrainingSegmentSerializer


@extend_schema_view(
    list=extend_schema(
        **description_points.exercise_training_segment_sets_list_endpoint
    ),
    retrieve=extend_schema(
        **description_points.exercise_training_segment_sets_detail_endpoint
    ),
    create=extend_schema(
        **description_points.exercise_training_segment_sets_create_endpoint
    ),
    update=extend_schema(
        **description_points.exercise_training_segment_sets_update_endpoint
    ),
    destroy=extend_schema(
        **description_points.exercise_training_segment_sets_delete_endpoint
    ),
    partial_update=extend_schema(
        **description_points.exercise_training_segment_sets_patch_endpoint
    ),
)
class SetViewSet(viewsets.ModelViewSet):
    """
    Обеспечивает представление сетов для выполнения CRUD операций.

    Этот класс позволяет управлять сетами, связанными
    с упражнением в тренировке, включая:
    - создание новых сетов
    - получение информации о конкретном сете
    - обновление существующих сетов
    - удаление сетов
    """

    queryset = Set.objects.all()

    def get_serializer_class(self, *args, **kwargs):
        """
        Возвращает класс сериализатора в зависимости от действия.

        Если действие - это получение списка или детальной информации (retrieve),
        используется SetSerializer. В противном случае используется SetCreateSerializer.
        """
        if self.action in ("list", "retrive"):
            return SetSerializer

        return SetCreateSerializer

    def get_queryset(self):
        """
        Возвращает набор сетов для конкретного упражнения тренировки.

        Метод извлекает идентификатор упражнения тренировки из параметров
        URL и возвращает все результаты для этого упражнения.
        """
        exercise = get_object_or_404(
            ExerciseTrainingSegment, id=self.kwargs["ex_train_segment_id"]
        )
        return exercise.results.all()

    def perform_create(self, serializer):
        """
        Сохраняет новый сет, связанный с определенным упражнением тренировки.

        Метод извлекает информацию о упражнении тренировки из параметров
        URL и сохраняет новый сет с соответствующими данными.
        """
        exercise = get_object_or_404(
            ExerciseTrainingSegment, id=self.kwargs["ex_train_segment_id"]
        )
        serializer.save(excercise=exercise)
