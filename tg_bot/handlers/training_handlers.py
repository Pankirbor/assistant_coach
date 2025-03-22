from aiogram import Router, types
from aiogram.filters import Command

training_router = Router()


# Обработчик для перехода в мини-приложение
@training_router.message(Command("training"))
async def open_training_app(message: types.Message):
    markup = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(
                    text="Открыть мини-приложение",
                    web_app=types.WebAppInfo(
                        url="https://chastely-revived-grayling.cloudpub.ru"
                    ),
                )
            ]
        ],
        resize_keyboard=True,  # Опционально: автоматическое изменение размера клавиатуры
    )

    await message.reply(
        "Нажмите кнопку ниже, чтобы открыть мини-приложение", reply_markup=markup
    )
