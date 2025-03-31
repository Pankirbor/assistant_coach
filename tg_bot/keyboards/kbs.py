import os
import logging

from aiogram.types import ReplyKeyboardMarkup, WebAppInfo, InlineKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

from config import settings

logger = logging.getLogger(__file__)


def main_keyboard(telegram_id: int) -> ReplyKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    url_training_plan = f"{settings.FRONT_SITE}?telegramId={telegram_id}"
    url_admin_site = f"{settings.BACK_SITE}admin"
    kb.button(text="📝 Начать тренировку", web_app=WebAppInfo(url=url_training_plan))
    if telegram_id in settings.ADMIN_IDS:
        kb.button(text="🌐 AdminPanel", web_app=WebAppInfo(url=url_admin_site))

    kb.adjust(1)
    return kb.as_markup(resize_keyboard=True)


def back_keyboard() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="🔙 Назад")
    kb.adjust(1)
    return kb.as_markup(resize_keyboard=True)


def app_keyboard(telegram_id: int) -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    url_training_plan = f"{settings.FRONT_SITE}?telegramId={telegram_id}"
    kb.button(text="📝 Начать тренировку", web_app=WebAppInfo(url=url_training_plan))
    kb.adjust(1)
    return kb.as_markup()
