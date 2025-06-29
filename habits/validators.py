from rest_framework.exceptions import ValidationError

from habits.models import Habit

def validate_habit(data):
    # Проверка 1: нельзя указать и вознаграждение, и связанную привычку
    if data.get("reward") and data.get("related_habit"):
        raise ValidationError(
            "Выберите что-то одно: вознаграждение или связанную привычку."
        )

    # Проверка 2: у приятной привычки нет вознаграждения или связанной привычки
    if data.get("is_pleasant") and (data.get("reward") or data.get("related_habit")):
        raise ValidationError(
            "Приятная привычка не может иметь вознаграждение или быть связанной."
        )

    # Проверка 3: время выполнения должно быть <= 120 секунд
    if data.get("duration", 0) > 120:
        raise ValidationError("Время выполнения не должно превышать 120 секунд.")

    # Проверка 4: периодичность должна быть от 1 до 7 дней
    if data.get("frequency", 1) < 1 or data.get("frequency", 1) > 7:
        raise ValidationError("Периодичность должна быть от 1 до 7 дней.")
