from rest_framework import generics, viewsets
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated

from habit.models import HabitGood, HabitNice
from habit.paginators import ListPaginator
from habit.permissions import IsOwner
from habit.serliazers import HabitGoodSerializer, HabitNiceSerializer


#   APIView для полезных привычек

class HabitGoodCreateAPIView(generics.CreateAPIView):
    """APIView для создания полезной привычки"""
    serializer_class = HabitGoodSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        new_lesson = serializer.save()
        new_lesson.owner = self.request.user
        new_lesson.save()


class HabitGoodPublicListAPIView(generics.ListAPIView):
    """APIView для просмотра списка публичных полезных привычек"""
    serializer_class = HabitGoodSerializer
    queryset = HabitGood.objects.filter(public=True)
    permission_classes = [IsAuthenticated]


class HabitGoodListAPIView(generics.ListAPIView):
    """APIView для просмотра списка полезных привычек"""
    serializer_class = HabitGoodSerializer
    queryset = HabitGood.objects.all()
    permission_classes = [IsAuthenticated]

    filter_backends = [OrderingFilter]
    ordering_fields = ('id',)
    pagination_class = ListPaginator

    def get_queryset(self):
        pk = self.request.user
        self.queryset = HabitGood.objects.filter(owner_id=pk)
        return self.queryset

    # def list(self, request, *args, **kwargs):
    #     queryset = HabitGood.objects.filter(owner_id=request.get['id'])
    #     super().list(self, request, *args, **kwargs)


class HabitGoodRetrieveAPIView(generics.RetrieveAPIView):
    """APIView для просмотра одной полезной привычки"""
    serializer_class = HabitGoodSerializer
    queryset = HabitGood.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class HabitGoodUpdateAPIView(generics.UpdateAPIView):
    """APIView для изменения полезной привычки"""
    serializer_class = HabitGoodSerializer
    queryset = HabitGood.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class HabitGoodDestroyAPIView(generics.DestroyAPIView):
    """APIView для удаления полезной привычки"""
    queryset = HabitGood.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


#   APIViewSet для приятных привычек


class HabitNiceViewSet(viewsets.ModelViewSet):
    """ViewSet для приятных привычек """
    serializer_class = HabitNiceSerializer
    queryset = HabitNice.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = ListPaginator

    def get_permissions(self):
        if self.action == 'CREATE':
            self.permission_classes = [IsAuthenticated]
        else:
            self.permission_classes = [IsAuthenticated, IsOwner]

        return super().get_permissions()

    def perform_create(self, serializer):
        new_habit_nice = serializer.save()
        new_habit_nice.owner = self.request.user
        new_habit_nice.save()
