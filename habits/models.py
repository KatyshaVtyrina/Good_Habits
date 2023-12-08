from django.db import models

from config import settings

NULLABLE = {'blank': True, 'null': True}


class Habit(models.Model):
    """Модель, описывающая привычку"""

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='создатель')
    place = models.CharField(max_length=100, verbose_name='место выполнения привычки')
    time = models.DateTimeField(verbose_name='время')
    action = models.CharField(max_length=100, verbose_name='действие')
    is_pleasant = models.BooleanField(verbose_name='признак приятной привычки')
    related_habit = models.ForeignKey('self', on_delete=models.SET_NULL,
                                      verbose_name='связанная привычка', **NULLABLE)
    periodicity = models.PositiveIntegerField(default=1, verbose_name='периодичность в днях')
    reward = models.CharField(max_length=100, verbose_name='вознаграждение', **NULLABLE)
    time_to_complete = models.TimeField(verbose_name='время на выполнение привычки')

    class Meta:
        verbose_name = 'привычка'
        verbose_name_plural = 'привычки'

    def __str__(self):
        return f'Привычка - {self.action}, место выполнения - {self.place} '
