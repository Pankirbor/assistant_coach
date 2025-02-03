from drf_spectacular.utils import OpenApiResponse
from .serializers import (
    ExerciseTrainingSegmentSerializer,
    SetCreateSerializer,
    SetSerializer,
    UserSerializer,
    WorkoutSerializer,
)

user_list_endpoint = {
    "summary": "Получение информации обо всех пользователях",
    "description": "Возвращает список всех зарегистрированных пользователей.",
    "responses": {
        200: OpenApiResponse(
            response=UserSerializer(many=True), description="Список всех пользователей"
        )
    },
}

user_detail_endpoint = {
    "summary": "Получение информации о пользователе",
    "description": "Возвращает информацию о пользователе по его ID.",
    "responses": {
        200: OpenApiResponse(
            response=UserSerializer(many=True), description="Информация о пользователе"
        ),
        404: OpenApiResponse(description="Пользователь не найден"),
    },
}

user_create_endpoint = {
    "summary": "Регистрация пользователя",
    "description": "Создаёт нового пользователя.",
    "responses": {
        201: OpenApiResponse(
            response=UserSerializer(many=True),
            description="Пользователь успешно создан",
        ),
        400: OpenApiResponse(description="Ошибки валидации"),
    },
}

user_delete_endpoint = {
    "summary": "Удаление пользователя",
    "description": "Удаляет пользователя по его ID. Если пользователь не найден, возвращает ошибку.",
    "responses": {
        200: OpenApiResponse(description="Пользователь успешно удалён"),
        404: OpenApiResponse(description="Пользователь не найден"),
        400: OpenApiResponse(description="ID пользователя не предоставлен"),
    },
}

user_put_endpoint = {
    "summary": "Обновление данных пользователя",
    "description": "Обновляет пользователя по его ID. Требуется передать все обязательные поля. Если пользователь не найден, возвращает ошибку.",
    "responses": {
        200: OpenApiResponse(
            response=UserSerializer, description="Данные успешно обновлены"
        ),
        404: OpenApiResponse(description="Пользователь не найден"),
        400: OpenApiResponse(
            description="ID пользователя не предоставлен или отсутствуют обязательные поля."
        ),
    },
}


# Эндпоинт для получения списка всех тренировок
workouts_list_endpoint = {
    "summary": "Получение списка тренировок",
    "description": "Возвращает список всех доступных тренировок.",
    "responses": {
        200: OpenApiResponse(
            response=WorkoutSerializer(many=True), description="Список тренировок"
        ),
    },
}

# Эндпоинт для получения информации о конкретной тренировке
workouts_detail_endpoint = {
    "summary": "Получение информации о тренировке",
    "description": "Возвращает информацию о тренировке по её ID.",
    "responses": {
        200: OpenApiResponse(
            response=WorkoutSerializer, description="Информация о тренировке"
        ),
        404: OpenApiResponse(description="Тренировка не найдена"),
    },
}

# Эндпоинт для создания новой тренировки
workouts_create_endpoint = {
    "summary": "Создание новой тренировки",
    "description": "Создает новую тренировку и возвращает её информацию.",
    "responses": {
        201: OpenApiResponse(
            response=WorkoutSerializer, description="Тренировка успешно создана"
        ),
        400: OpenApiResponse(description="Ошибка валидации данных"),
    },
}

# Эндпоинт для обновления существующей тренировки
workouts_update_endpoint = {
    "summary": "Обновление информации о тренировке",
    "description": "Обновляет информацию о тренировке по её ID и возвращает обновленную информацию.",
    "responses": {
        200: OpenApiResponse(
            response=WorkoutSerializer, description="Тренировка успешно обновлена"
        ),
        404: OpenApiResponse(description="Тренировка не найдена"),
        400: OpenApiResponse(description="Ошибка валидации данных"),
    },
}

# Эндпоинт для частичного обновления существующей тренировки
workouts_patch_endpoint = {
    "summary": "Частичное обновление информации о тренировке",
    "description": "Обновляет информацию о тренировке по её ID и возвращает обновленную информацию.",
    "responses": {
        200: OpenApiResponse(
            response=WorkoutSerializer, description="Тренировка успешно обновлена"
        ),
        404: OpenApiResponse(description="Тренировка не найдена"),
        400: OpenApiResponse(description="Ошибка валидации данных"),
    },
}

# Эндпоинт для удаления тренировки
workouts_delete_endpoint = {
    "summary": "Удаление тренировки",
    "description": "Удаляет тренировку по её ID.",
    "responses": {
        204: OpenApiResponse(description="Тренировка успешно удалена"),
        404: OpenApiResponse(description="Тренировка не найдена"),
    },
}

# Эндпоинт для получения списка всех сегментов тренировок
exercise_training_segment_list_endpoint = {
    "summary": "Получение списка упражнений из всех сегментов тренировок",
    "description": "Возвращает список всех доступных упражнений из сегментов тренировок.",
    "responses": {
        200: OpenApiResponse(
            response=ExerciseTrainingSegmentSerializer(many=True),
            description="Список упражнений из сегментов тренировок",
        ),
    },
}

# Эндпоинт для получения информации о конкретном сегменте тренировки
exercise_training_segment_detail_endpoint = {
    "summary": "Получение информации о запланированном упражнении",
    "description": "Возвращает информацию о запланированном упражнении по его ID.",
    "responses": {
        200: OpenApiResponse(
            response=ExerciseTrainingSegmentSerializer,
            description="Информация о запланированном упражнении",
        ),
        404: OpenApiResponse(description="Упражнение не найдено"),
    },
}

# Эндпоинт для создания нового сегмента тренировки
exercise_training_segment_create_endpoint = {
    "summary": "Создание нового упражнении для сегмента тренировки",
    "description": "Создает новое упражнение для сегмента тренировки и возвращает его информацию.",
    "responses": {
        201: OpenApiResponse(
            response=ExerciseTrainingSegmentSerializer,
            description="Упражнение для сегмента тренировки успешно создано",
        ),
        400: OpenApiResponse(description="Ошибка валидации данных"),
    },
}

# Эндпоинт для обновления существующего сегмента тренировки
exercise_training_segment_update_endpoint = {
    "summary": "Обновление информации об упражнении для сегмента тренировки",
    "description": "Обновляет информацию об упражнении для сегмента тренировки по его ID и возвращает обновленную информацию.",
    "responses": {
        200: OpenApiResponse(
            response=ExerciseTrainingSegmentSerializer,
            description="Упражнение для сегмента тренировки успешно обновлено",
        ),
        404: OpenApiResponse(description="Упражнение не найдено"),
        400: OpenApiResponse(description="Ошибка валидации данных"),
    },
}

# Эндпоинт для частичного обновления существующей тренировки
exercise_training_segment_patch_endpoint = {
    "summary": "Частичное обновление информации об упражнении для сегмента тренировки",
    "description": "Частичное обновляет информацию об упражнении для сегмента тренировки по её ID и возвращает обновленную информацию.",
    "responses": {
        200: OpenApiResponse(
            response=ExerciseTrainingSegmentSerializer,
            description="Упражнение для сегмента тренировки успешно обновлено",
        ),
        404: OpenApiResponse(description="Упражнение не найдено"),
        400: OpenApiResponse(description="Ошибка валидации данных"),
    },
}

# Эндпоинт для удаления сегмента тренировки
exercise_training_segment_delete_endpoint = {
    "summary": "Удаление упражнении для сегмента тренировки",
    "description": "Удаляет упражнении для сегмента тренировки по его ID.",
    "responses": {
        204: OpenApiResponse(
            description="Упражнение для сегмента тренировки успешно удалено"
        ),
        404: OpenApiResponse(
            description="Упражнение для сегмента тренировки не найдено"
        ),
    },
}


# Эндпоинт для получения списка наборов в сегменте тренировки
exercise_training_segment_sets_list_endpoint = {
    "summary": "Получение списка результатов подходов в упражнении тренировки",
    "description": "Возвращает список всех результатов подходов, связанных с упражнением по его ID.",
    "responses": {
        200: OpenApiResponse(
            response=SetSerializer(many=True),
            description="Список результатов подходов в упражнении",
        ),
        404: OpenApiResponse(description="Упражнение не найдено"),
    },
}

# Эндпоинт для создания нового набора в сегменте тренировки

exercise_training_segment_sets_create_endpoint = {
    "summary": "Создание нового подхода с результатами в упражнении",
    "description": "Создает новый подход в упражнении и возвращает его информацию.",
    "responses": {
        201: OpenApiResponse(
            response=SetCreateSerializer, description="Подход успешно создан"
        ),
        400: OpenApiResponse(description="Ошибка валидации данных"),
        404: OpenApiResponse(description="Упражнение не найдено"),
    },
}

# Эндпоинт для получения информации о конкретном наборе в сегменте тренировки
exercise_training_segment_sets_detail_endpoint = {
    "summary": "Получение информации о результатах подхода в упражнении",
    "description": "Возвращает информацию о подходе по его ID в контексте упражнения тренировки.",
    "responses": {
        200: OpenApiResponse(
            response=SetSerializer, description="Информация о подходе"
        ),
        404: OpenApiResponse(description="Подход или упражнение не найдены"),
    },
}

# Эндпоинт для обновления существующего набора в сегменте тренировки
exercise_training_segment_sets_update_endpoint = {
    "summary": "Обновление информации о подходе в упражнении",
    "description": "Обновляет информацию о подходе по его ID в контексте упражнения тренировки и возвращает обновленную информацию.",
    "responses": {
        200: OpenApiResponse(
            response=SetSerializer, description="Подход успешно обновлен"
        ),
        404: OpenApiResponse(description="Подход или упражнение не найдены"),
        400: OpenApiResponse(description="Ошибка валидации данных"),
    },
}

# Эндпоинт для обновления существующего набора в сегменте тренировки
exercise_training_segment_sets_patch_endpoint = {
    "summary": "Частичное обновление информации о подходе в упражнении",
    "description": "Частичное обновляет информацию о подходе по его ID в контексте упражнения тренировки и возвращает обновленную информацию.",
    "responses": {
        200: OpenApiResponse(
            response=SetSerializer, description="Подход успешно обновлен"
        ),
        404: OpenApiResponse(description="Подход или упражнение не найдены"),
        400: OpenApiResponse(description="Ошибка валидации данных"),
    },
}

# Эндпоинт для удаления набора из сегмента тренировки
exercise_training_segment_sets_delete_endpoint = {
    "summary": "Удаление подхода из упражнения тренировки",
    "description": "Удаляет подход по его ID из упражнения тренировки.",
    "responses": {
        204: OpenApiResponse(description="Подход успешно удален"),
        404: OpenApiResponse(description="Подход или упражнение не найдены"),
    },
}
