from habits.models import Habit
import json


from django_celery_beat.models import PeriodicTask, \
    IntervalSchedule


class Reminder:
    """Класс, описывающий расписание отправки напоминаний о привычке"""

    def __init__(self, habit: Habit):
        self.habit = habit

    def create_reminder(self):

        # Создаем расписание
        schedule, created = IntervalSchedule.objects.get_or_create(
            every=self.habit.periodicity,
            period=IntervalSchedule.DAYS,
        )

        # Создаем задачу для повторения
        PeriodicTask.objects.create(
            interval=schedule,
            name=f'send_telegram_message_{self.habit.id}',
            task='habits.tasks.send_telegram_message',
            args=json.dumps([self.habit.id]),
        )
