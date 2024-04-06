
from rest_framework import routers

from users.views import UserViewSet

from users.apps import UsersConfig

app_name = UsersConfig.name

urlpatterns = [
]
router = routers.SimpleRouter()
router.register(r'user', UserViewSet)

urlpatterns += router.urls
