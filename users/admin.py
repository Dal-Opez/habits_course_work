from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class CustomUserAdmin(UserAdmin):
    # Убираем username из полей и сортировки
    ordering = ("email",)  # Сортируем по email
    list_display = ("email", "is_staff")  # Поля для отображения

    # Изменяем fieldsets для формы редактирования
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal info", {"fields": ("telegram_id",)}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )

    # Изменяем add_fieldsets для формы создания
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )


admin.site.register(User, CustomUserAdmin)
