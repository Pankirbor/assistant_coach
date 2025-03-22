import asyncio
import logging
import os

from aiogram import Bot, Dispatcher

from handlers import commands_router, training_router

API_TOKEN = os.environ.get(
    "BOT_TOKEN", "7767038065:AAHT-I6mUtbyolIyVCsmJvac0kwQFbybFJw"
)

logger = logging.getLogger(__name__)


async def main():
    """Функция запуска бота."""

    logging.basicConfig(
        level=logging.INFO,
        format="%(filename)s:%(lineno)d #%(levelname)-8s "
        "[%(asctime)s] - %(name)s - %(message)s",
    )
    logger.info("Starting bot")
    bot = Bot(token=API_TOKEN)
    dp = Dispatcher()
    dp.include_router(commands_router)
    dp.include_router(training_router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
