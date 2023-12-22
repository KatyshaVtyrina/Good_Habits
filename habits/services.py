
from django_celery_beat.models import PeriodicTask, CrontabSchedule


def create_reminder(habit):
    """Создание расписания и задачи"""
    # Создаем расписание
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
    )


def delete_reminder(habit):
    """Удаление задачи"""
    task_name = f'send_telegram_message_{habit.id}'
    PeriodicTask.objects.filter(name=task_name).delete()


def update_reminder(habit):
    """Обновление задачи"""
    delete_reminder(habit)
    create_reminder(habit)
