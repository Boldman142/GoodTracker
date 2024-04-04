from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from users.models import User
from users.permissions import AccountOwner
from users.serliazers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def perform_create(self, serializer):
        new_user = serializer.save()

        new_user.set_password(new_user.password)
        new_user.save()

    def get_permissions(self):
        if self.action not in ['create']:
            self.permission_classes = [IsAuthenticated]
            if self.action in ['update', 'retrieve', 'destroy']:
                self.permission_classes = [IsAuthenticated, AccountOwner]

        return super().get_permissions()
