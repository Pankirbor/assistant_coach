import logging
import aiohttp

from aiogram import Bot, Router, types
from aiogram.filters import Command

from config import settings
from utils.utils import greet_user

commands_router = Router()

logger = logging.getLogger(__file__)


@commands_router.message(Command("start"))
async def send_welcome(message: types.Message):
    logger.info(
        f"Сработал обработчик команды start для user {message.from_user.full_name}"
    )

    await message.reply("Привет! Я бот для управления твоими тренировками.")

    API_USERS_URL = f"{settings.FRONT_SITE}api/users/"  # Замените на ваш домен
    TELEGRAM_ID = message.from_user.id

    user_data = {
        "telegram_id": TELEGRAM_ID,
        "username": message.from_user.username,
        "first_name": message.from_user.first_name,
        "last_name": message.from_user.last_name,
        "email": "example@fucke.ru",  # Можно запросить позже
    }
    logger.info(f"User info for POST {user_data}")

    headers = {"Content-Type": "application/json"}

    try:
        async with aiohttp.ClientSession() as session:
            # 1. Сначала проверяем существование пользователя
            check_url = f"{API_USERS_URL}?telegram_id={TELEGRAM_ID}"
            async with session.get(check_url, headers=headers) as response:
                if response.status == 200:
                    data = await response.json()
                    logger.info(f"User info for GET {data}")
                    # Если пользователь найден
                    if data and len(data) > 0:
                        await greet_user(message=message, is_new_user=False)
                        return

            # 2. Если пользователь не найден - создаём нового
            async with session.post(
                API_USERS_URL, json=user_data, headers=headers
            ) as response:
                if response.status == 201:
                    await greet_user(message, is_new_user=True)
                    logger.info("Успешно сохранен пользователь")

                else:
                    error_text = await response.text()
                    await message.answer(f"Ошибка при сохранении: {error_text}")
                    logger.info(f"Ошибка при сохранении: {error_text}")

    except aiohttp.ClientError as e:
        await message.answer(f"Ошибка соединения с сервером: {str(e)}")
        logger.info(f"Ошибка соединения с сервером: {str(e)}")

    except Exception as e:
        await message.answer(f"Неожиданная ошибка: {str(e)}")
        logger.info(f"Неожиданная ошибка: {str(e)}")


# Обработчик команды /help
@commands_router.message(Command("help"))
async def send_help(message: types.Message):
    logger.info(
        f"Сработал обработчик команды help для user {message.from_user.full_name}"
    )
    await message.reply("Здесь будет инструкция по использованию бота.")
