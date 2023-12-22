from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from habits.models import Habit

from habits.validators import (validate_related_habit_or_reward, validate_time_to_complete,
                               validate_related_habit_is_pleasant, validate_is_pleasant,
                               validate_periodicity)
from users.models import User


class HabitSerializer(serializers.ModelSerializer):
    """Класс-сериализатор для модели Habit"""

    class Meta:
        model = Habit
        fields = '__all__'

    def validate(self, data):
        """
        Валидаторы для модели Habit.
        """
        validate_related_habit_or_reward(data, self.instance)
        validate_time_to_complete(data)
        validate_related_habit_is_pleasant(data)
        validate_is_pleasant(data, self.instance)
        validate_periodicity(data)
        return data


class HabitViewSerializer(serializers.ModelSerializer):
    user = SlugRelatedField(slug_field='email', queryset=User.objects.all())
    related_habit = SlugRelatedField(slug_field='action', queryset=Habit.objects.all())

    class Meta:
        model = Habit
        fields = '__all__'
