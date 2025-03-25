import logging
import aiohttp

from aiogram import Router, types
from aiogram.filters import Command

commands_router = Router()

logger = logging.getLogger(__file__)


@commands_router.message(Command("start"))
async def send_welcome(message: types.Message):
    await message.reply("Привет! Я бот для управления твоими тренировками.")

    API_BASE_URL = "https://chastely-revived-grayling.cloudpub.ru/api/users/"  # Замените на ваш домен
    TELEGRAM_ID = message.from_user.id

    user_data = {
        "telegram_id": TELEGRAM_ID,
        "username": message.from_user.username,
        "first_name": message.from_user.first_name,
        "last_name": message.from_user.last_name,
        "email": "example@fucke.ru",  # Можно запросить позже
    }
    logger.debug(f"User info for POST {user_data}")

    headers = {"Content-Type": "application/json"}

    try:
        async with aiohttp.ClientSession() as session:
            # 1. Сначала проверяем существование пользователя
            check_url = f"{API_BASE_URL}?telegram_id={TELEGRAM_ID}"
            async with session.get(check_url, headers=headers) as response:
                if response.status == 200:
                    data = await response.json()
                    logger.debug(f"User info for GET {data}")
                    # Если пользователь найден
                    if data and len(data) > 0:
                        await message.answer("С возвращением! Вы уже зарегистрированы.")
                        return

            # 2. Если пользователь не найден - создаём нового
            async with session.post(
                API_BASE_URL, json=user_data, headers=headers
            ) as response:
                if response.status == 201:
                    await message.answer("Добро пожаловать! Ваши данные сохранены.")
                    logger.debug("Успешно сохранен пользователь")

                else:
                    error_text = await response.text()
                    await message.answer(f"Ошибка при сохранении: {error_text}")
                    logger.debug(f"Ошибка при сохранении: {error_text}")

    except aiohttp.ClientError as e:
        await message.answer(f"Ошибка соединения с сервером: {str(e)}")
        logger.debug(f"Ошибка соединения с сервером: {str(e)}")

    except Exception as e:
        await message.answer(f"Неожиданная ошибка: {str(e)}")
        logger.debug(f"Неожиданная ошибка: {str(e)}")


# Обработчик команды /help
@commands_router.message(Command("help"))
async def send_help(message: types.Message):
    await message.reply("Здесь будет инструкция по использованию бота.")
