from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from habits.models import Habit
from habits.permissions import IsUser
from habits.serializers import HabitSerializer
from habits.services import create_reminder
from paginators import HabitPaginator


class HabitCreateAPIView(generics.CreateAPIView):
    """Создание привычки"""
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]

    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     super().perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)
    #     instance = Habit.objects.get(id=serializer.data['id'])
    #     print(instance)
    #     # reminder = Reminder(instance)
    #     # create_reminder(instance)
    #
    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    # def perform_create(self, serializer):
    #     """Автоматическое сохранение владельца при создании объекта"""
    #     serializer.save(user=self.request.user)
    #
    def perform_create(self, serializer):
        new_habit = serializer.save()
        new_habit.user = self.request.user
        new_habit.save()
        create_reminder(new_habit)


class HabitListAPIView(generics.ListAPIView):
    """Просмотр привычек"""
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
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
    serializer_class = HabitSerializer
    pagination_class = HabitPaginator
    permission_classes = [IsAuthenticated]


class HabitDetailAPIView(generics.RetrieveAPIView):
    """Просмотр детальной информации о привычке"""
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsUser]


class HabitUpdateAPIView(generics.UpdateAPIView):
    """Редактирование привычки"""
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsUser]


class HabitDeletePIView(generics.DestroyAPIView):
    """Удаление привычки"""
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsUser]
