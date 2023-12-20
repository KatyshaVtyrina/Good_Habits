import requests
from celery import shared_task

from config import settings
from habits.models import Habit


@shared_task
def send_telegram_message(habit_id):
    # print(habit_id[0])
    habit = Habit.objects.get(pk=habit_id)

    requests.post(
        url=f'{settings.TELEGRAM_URL}{settings.TELEGRAM_BOT_API_KEY}/sendMessage',
        data={
            'chat_id': habit.user.tg_id,
            'text': f'Пора выполнить привычку {habit.action}, место выполнения - {habit.place}, '
                    f'время выполнения - {habit.time}'
        }
    )
