import logging

from aiogram import Router, types
from aiogram.filters import Command

training_router = Router()

logger = logging.getLogger(__file__)


# Обработчик для перехода в мини-приложение
@training_router.message(Command("training"))
async def open_training_app(message: types.Message):
    telegram_id = message.from_user.id
    url_get_trainplan = (
        f"https://chastely-revived-grayling.cloudpub.ru/?telegramId={telegram_id}"
    )

    logger.info(f"Url for request: {url_get_trainplan=}")
    markup = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(
                    text="Открыть мини-приложение",
                    web_app=types.WebAppInfo(url=url_get_trainplan),
                )
            ]
        ],
        resize_keyboard=True,  # Опционально: автоматическое изменение размера клавиатуры
    )

    await message.reply(
        "Нажмите кнопку ниже, чтобы открыть мини-приложение", reply_markup=markup
    )
