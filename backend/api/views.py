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
from .description_points import (
    user_list_endpoint,
    user_detail_endpoint,
    user_create_endpoint,
    user_put_endpoint,
    user_delete_endpoint,
)
from workout.models import Set, Workout, ExerciseTrainingSegment
from users.models import CustomUser


@extend_schema_view(
    list=extend_schema(**user_list_endpoint),
    retrieve=extend_schema(**user_detail_endpoint),
    create=extend_schema(**user_create_endpoint),
    update=extend_schema(**user_put_endpoint),
    destroy=extend_schema(**user_delete_endpoint),
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

    @action(methods=["get"], detail=False, url_path="next_workout")
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


class ExerciseTrainingSegmentViewSet(viewsets.ModelViewSet):
    queryset = ExerciseTrainingSegment.objects.all()
    serializer_class = ExerciseTrainingSegmentSerializer


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
