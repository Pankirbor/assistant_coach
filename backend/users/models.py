from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    telegram_id = models.IntegerField(default=0, blank=True, verbose_name="Телеграм id")
    email = models.EmailField(
        verbose_name="Электронная почта",
        max_length=254,
        unique=True,
        blank=False,
        help_text=("Укажите свой email"),
        error_messages={
            "unique": ("Этот email уже зарегистрирован."),
        },
    )
    password = models.CharField(
        verbose_name="Пароль",
        max_length=150,
        help_text=("Введите пароль"),
    )

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.username
