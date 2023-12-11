from rest_framework import generics

from habits.models import Habit
from habits.serializers import HabitSerializer


class HabitCreateAPIView(generics.CreateAPIView):
    """Создание привычки"""
    serializer_class = HabitSerializer


class HabitListAPIView(generics.ListAPIView):
    """Просмотр всех привычек"""
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer


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
