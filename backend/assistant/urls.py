from django.contrib import admin
from django.urls import path, include

from drf_spectacular.views import (
    SpectacularRedocView,
    SpectacularSwaggerView,
    SpectacularAPIView,
)


urlpatterns = [
    path("api_v1/", include("api.urls", namespace="api")),
    # Генерация OpenAPI схемы
    path("api_v1/schema/", SpectacularAPIView.as_view(), name="schema"),
    # Swagger UI
    path(
        "api_v1/docs/swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    # Redoc
    path(
        "api_v1/docs/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
    path("admin/", admin.site.urls),
]
