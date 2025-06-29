# Создаем файл tasks.py в приложении habits
from celery import shared_task
from config.telegram_service import TelegramBot
from django.conf import settings

@shared_task
def send_telegram_notification(telegram_id, message):
    if telegram_id and settings.TELEGRAM_BOT_TOKEN:
        TelegramBot.send_message(telegram_id, message)

@shared_task
def check_habits_and_notify():
    from django.utils import timezone
    from .models import Habit
    habits = Habit.objects.filter(
        last_completed__lte=timezone.now() - timedelta(days=1)
    )
    for habit in habits:
        if habit.user.telegram_id:
            send_telegram_notification.delay(
                habit.user.telegram_id,
                f"Напоминание: {habit.action} в {habit.time}"
            )