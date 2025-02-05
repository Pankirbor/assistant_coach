from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    """
    Модель пользователя.

    Расширяет стандартную модель пользователя Django, добавляя
    дополнительные поля для хранения идентификатора Telegram и
    электронной почты.

    Attributes:
        telegram_id (int): Идентификатор Telegram пользователя.
        email (str): Электронная почта пользователя, уникальная для каждого.
        password (str): Пароль пользователя.
    """

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
        """
        Возвращает строковое представление пользователя.

        Returns:
            str: Имя пользователя (username).
        """
        return self.username
