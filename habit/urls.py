from django.urls import path
from rest_framework import routers

from habit.apps import HabitConfig
from habit.views import (HabitNiceViewSet, HabitGoodCreateAPIView, HabitGoodListAPIView,
                         HabitGoodRetrieveAPIView, HabitGoodUpdateAPIView,
                         HabitGoodDestroyAPIView, HabitGoodPublicListAPIView)

app_name = HabitConfig.name

urlpatterns = [
    path('good/create/', HabitGoodCreateAPIView.as_view(), name='habit_good_create'),
    path('good/', HabitGoodListAPIView.as_view(), name='habit_good_list'),
    path('good/public/', HabitGoodPublicListAPIView.as_view(), name='habit_good_pub_list'),
    path('good/<int:pk>/', HabitGoodRetrieveAPIView.as_view(), name='habit_good_get'),
    path('good/update/<int:pk>/', HabitGoodUpdateAPIView.as_view(), name='habit_good_update'),
    path('good/delete/<int:pk>/', HabitGoodDestroyAPIView.as_view(), name='habit_good_del'),
]

router = routers.SimpleRouter()
router.register(r'nice', HabitNiceViewSet)

urlpatterns += router.urls
