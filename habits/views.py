from rest_framework import generics

from habits.models import Habit
from habits.serializers import HabitSerializer
from paginators import HabitPaginator


class HabitCreateAPIView(generics.CreateAPIView):
    """Создание привычки"""
    serializer_class = HabitSerializer


class HabitListAPIView(generics.ListAPIView):
    """Просмотр всех привычек"""
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    pagination_class = HabitPaginator


class HabitPublicListAPIView(generics.ListAPIView):
    """Просмотр публичных привычек"""
    queryset = Habit.objects.all().filter(is_public=True)
    serializer_class = HabitSerializer
    pagination_class = HabitPaginator


class HabitDetailAPIView(generics.RetrieveAPIView):
    """Просмотр детальной информации о привычке"""
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()


class HabitUpdateAPIView(generics.UpdateAPIView):
    """Редактирование привычки"""
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()


class HabitDeletePIView(generics.DestroyAPIView):
    """Удаление привычки"""
    queryset = Habit.objects.all()
