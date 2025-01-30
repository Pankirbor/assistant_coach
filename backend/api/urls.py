from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

app_name = "api"

router_v1 = DefaultRouter()
router_v1.register(
    "users",
    views.UserViewSet,
    basename="users",
)

router_v1.register(
    "workouts",
    views.WorkoutViewSet,
    basename="Workouts",
)

urlpatterns = [
    path("", include(router_v1.urls)),
    # path("", include("djoser.urls")),
    # path("auth/", include("djoser.urls.authtoken")),
]
