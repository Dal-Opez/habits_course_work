from rest_framework.exceptions import ValidationError

from habits.models import Habit


def validate_habit(data):
    # Проверка: нельзя указать и вознаграждение, и связанную привычку
    if data.get("reward") and data.get("related_habit"):
        raise ValidationError(
            "Выберите что-то одно: вознаграждение или связанную привычку."
        )

    # Проверка: у приятной привычки нет вознаграждения или связанной привычки
    if data.get("is_pleasant") and (data.get("reward") or data.get("related_habit")):
        raise ValidationError(
            "Приятная привычка не может иметь вознаграждение или быть связанной."
        )

    # Проверка: связанная привычка должна быть приятной
    if data.get("related_habit"):
        related_habit = Habit.objects.get(id=data["related_habit"])
        if not related_habit.is_pleasant:
            raise ValidationError("Связанная привычка должна быть приятной.")
