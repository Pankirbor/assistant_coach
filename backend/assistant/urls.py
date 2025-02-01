from django.contrib import admin
from django.urls import path, include

from drf_spectacular.views import (
    SpectacularRedocView,
    SpectacularSwaggerView,
    SpectacularAPIView,
)


urlpatterns = [
    path("api/", include("api.urls", namespace="api")),
    # Генерация OpenAPI схемы
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    # Swagger UI
    path(
        "api/docs/swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    # Redoc
    path(
        "api/docs/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
    path("admin/", admin.site.urls),
]
