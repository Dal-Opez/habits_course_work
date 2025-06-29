from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from users.models import User


class Habit(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Пользователь"
    )
    place = models.CharField(max_length=100, verbose_name="Место")
    time = models.TimeField(verbose_name="Время")
    action = models.CharField(max_length=200, verbose_name="Действие")
    is_pleasant = models.BooleanField(default=False, verbose_name="Приятная привычка")
    related_habit = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Связанная привычка",
    )
    frequency = models.PositiveIntegerField(
        default=1,
        validators=[MinValueValidator(1), MaxValueValidator(7)],
        verbose_name="Периодичность (дни)",
    )
    reward = models.CharField(max_length=200, blank=True, verbose_name="Вознаграждение")
    duration = models.PositiveIntegerField(
        validators=[MaxValueValidator(120)], verbose_name="Время на выполнение (сек)"
    )
    is_public = models.BooleanField(default=False, verbose_name="Публичная")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.action} в {self.time}"
