from rest_framework import viewsets, mixins, status
from rest_framework.response import Response

from ..models import User
from ..serializers import UserSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet,
                  mixins.RetrieveModelMixin,
                  mixins.CreateModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
            headers=headers
        )
