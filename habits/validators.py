import datetime

from rest_framework.serializers import ValidationError


def validate_related_habit_or_reward(value, instance):
    """Исключает одновременное указание связанной привычки и вознаграждения"""
    if instance is not None:
        related_habit = value.get('related_habit', instance.related_habit)
        reward = value.get('reward', instance.reward)
    else:
        related_habit = value.get('related_habit')
        reward = value.get('reward')

    if related_habit and reward:
        raise ValidationError("Нельзя указывать одновременно связанную привычку и вознаграждение")


def validate_time_to_complete(value):
    """Проверяет время выполнения привычки. Не может быть более двух минут"""
    if value.get("time_to_complete"):
        if value.get('time_to_complete') > datetime.time(hour=0, minute=2, second=0):
            raise ValidationError("Время выполнения не может быть более двух минут")


def validate_related_habit_is_pleasant(value):
    """Проверка связанной привычки на признак приятной привычки"""
    if value.get('related_habit') and not value.get('related_habit').is_pleasant:
        raise ValidationError("В связанные привычки могут попадать только привычки с признаком приятной привычки.")


def validate_is_pleasant(value, instance):
    """Проверка наличия вознаграждения и/или связанной привычки у приятной привычки"""
    if instance is not None:
        is_pleasant = value.get('is_pleasant', instance.is_pleasant)
        related_habit = value.get('related_habit', instance.related_habit)
        reward = value.get('reward', instance.reward)
    else:
        is_pleasant = value.get('is_pleasant')
        related_habit = value.get('related_habit')
        reward = value.get('reward')

    if is_pleasant:
        if related_habit or reward:
            raise ValidationError('У приятной привычки не может быть вознаграждения или связанной привычки.')


def validate_periodicity(value):
    """Проверка периодичности, не может быть реже, чем 1 раз в 7 дней."""
    if value.get('periodicity') and value.get('periodicity') > 7:
        raise ValidationError('Нельзя выполнять привычку реже, чем 1 раз в 7 дней.')
