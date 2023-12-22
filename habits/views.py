from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from habits.models import Habit
from habits.permissions import IsUser
from habits.serializers import HabitSerializer, HabitViewSerializer
from habits.services import create_reminder, delete_reminder, update_reminder
from paginators import HabitPaginator


class HabitCreateAPIView(generics.CreateAPIView):
    """Создание привычки"""
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        new_habit = serializer.save()
        new_habit.user = self.request.user
        new_habit.save()
        create_reminder(new_habit)


class HabitListAPIView(generics.ListAPIView):
    """Просмотр привычек"""
    queryset = Habit.objects.all()
    serializer_class = HabitViewSerializer
    pagination_class = HabitPaginator

    def get_queryset(self):
        """Если модератор - возвращается список всех привычек, если нет - список привычек
        авторизованного пользователя"""
        if self.request.user.is_authenticated:
            if self.request.user.is_staff:
                return self.queryset
            return self.queryset.filter(user=self.request.user)


class HabitPublicListAPIView(generics.ListAPIView):
    """Просмотр публичных привычек"""
    queryset = Habit.objects.all().filter(is_public=True)
    serializer_class = HabitViewSerializer
    pagination_class = HabitPaginator
    permission_classes = [IsAuthenticated]


class HabitDetailAPIView(generics.RetrieveAPIView):
    """Просмотр детальной информации о привычке"""
    serializer_class = HabitViewSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsUser]


class HabitUpdateAPIView(generics.UpdateAPIView):
    """Редактирование привычки"""
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsUser]

    def perform_update(self, serializer):
        """Обновление привычки и расписания по ней"""
        habit = serializer.save()
        update_reminder(habit)
        habit.save()


class HabitDeletePIView(generics.DestroyAPIView):
    """Удаление привычки"""
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsUser]

    def perform_destroy(self, instance):
        """Удаление привычки и напоминания по ней"""
        delete_reminder(instance)
        instance.delete()
