import datetime

from rest_framework.serializers import ValidationError


def validate_related_habit_or_reward(value):
    """Исключает одновременное указание связанной привычки и вознаграждения"""
    if value.get('related_habit') and value.get('reward'):
        raise ValidationError("Нельзя указывать одновременно связанную привычку и вознаграждение")


def validate_time_to_complete(value):
    """Проверяет время выполнения привычки. Не может быть более двух минут"""
    if value.get('time_to_complete') > datetime.time(hour=0, minute=2, second=0):
        raise ValidationError("Время выполнения не может быть более двух минут")


def validate_related_habit_is_pleasant(value):
    """Проверка связанной привычки на признак приятной привычки"""
    if value.get('related_habit') and not value.get('related_habit').is_pleasant:
        raise ValidationError("В связанные привычки могут попадать только привычки с признаком приятной привычки.")


def validate_is_pleasant(value):
    """Проверка наличия вознаграждения и/или связанной привычки у приятной привычки"""
    if value.get('is_pleasant'):
        if value.get('related_habit') or value.get('reward'):
            raise ValidationError('У приятной привычки не может быть вознаграждения или связанной привычки.')


def validate_periodicity(value):
    """Проверка периодичности, не может быть реже, чем 1 раз в 7 дней."""
    if value.get('periodicity') < 7:
        raise ValidationError('Нельзя выполнять привычку реже, чем 1 раз в 7 дней.')
