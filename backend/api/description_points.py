from drf_spectacular.utils import OpenApiResponse
from .serializers import UserSerializer

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
