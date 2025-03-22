from aiogram import Router, types
from aiogram.filters import Command

commands_router = Router()


@commands_router.message(Command("start"))
async def send_welcome(message: types.Message):
    await message.reply("Привет! Я бот для управления твоими тренировками.")


# Обработчик команды /help
@commands_router.message(Command("help"))
async def send_help(message: types.Message):
    await message.reply("Здесь будет инструкция по использованию бота.")
