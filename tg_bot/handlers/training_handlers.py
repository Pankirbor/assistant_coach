import logging

from aiogram import Router, types
from aiogram.filters import Command

from keyboards.kbs import app_keyboard


training_router = Router()

logger = logging.getLogger(__file__)


# Обработчик для перехода в мини-приложение
@training_router.message(Command("training"))
async def open_training_app(message: types.Message):
    telegram_id = message.from_user.id
    logger.info(
        f"Сработал обработчик команды training для user {message.from_user.full_name}"
    )
    await message.reply(
        "Нажмите кнопку ниже, чтобы открыть мини-приложение",
        reply_markup=app_keyboard(telegram_id),
    )
