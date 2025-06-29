import requests
import logging
from django.conf import settings

logger = logging.getLogger(__name__)


class TelegramBot:
    BASE_URL = f"https://api.telegram.org/bot{settings.TELEGRAM_BOT_TOKEN}/"

    @classmethod
    def send_message(cls, chat_id, text, parse_mode=None, disable_notification=False):
        url = f"{cls.BASE_URL}sendMessage"
        data = {
            "chat_id": chat_id,
            "text": text,
            "parse_mode": parse_mode,
            "disable_notification": disable_notification
        }

        try:
            response = requests.post(url, json=data)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            logger.error(f"Error sending Telegram message: {e}")
            return None