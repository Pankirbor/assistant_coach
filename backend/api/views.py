from rest_framework import viewsets
from drf_spectacular.utils import extend_schema_view, extend_schema

from .serializers import UserSerializer
from .description_points import (
    user_list_endpoint,
    user_detail_endpoint,
    user_create_endpoint,
    user_put_endpoint,
    user_delete_endpoint,
)
from users.models import CustomUser


@extend_schema_view(
    list=extend_schema(**user_list_endpoint),
    retrieve=extend_schema(**user_detail_endpoint),
    create=extend_schema(**user_create_endpoint),
    update=extend_schema(**user_put_endpoint),
    destroy=extend_schema(**user_delete_endpoint),
)
class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
