from datetime import datetime, timedelta

from habits.models import Habit
import json

from django_celery_beat.models import PeriodicTask, \
    IntervalSchedule, CrontabSchedule


# class Reminder:
#     """Класс, описывающий расписание отправки напоминаний о привычке"""
#
#     def __init__(self, habit: Habit):
#         self.habit = habit

def create_reminder(habit):
    # Создаем расписание
    # schedule, created = IntervalSchedule.objects.get_or_create(
    #     every=habit.periodicity,
    #     period=IntervalSchedule.DAYS,
    # )

    schedule, created = CrontabSchedule.objects.get_or_create(
        minute=habit.time.minute,
        hour=habit.time.hour,
        day_of_month=f'*/{habit.periodicity}',
        month_of_year='*',
        day_of_week='*',
        timezone='Europe/Moscow'
    )

    # Создаем задачу для повторения
    PeriodicTask.objects.create(
        crontab=schedule,
        name=f'send_telegram_message_{habit.id}',
        task='habits.tasks.send_telegram_message',
        args=[habit.id],
        # kwargs=json.dumps({'habit_id': self.habit.id}),
    )
