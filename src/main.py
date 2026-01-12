import asyncio
import logging

from aiogram import Dispatcher, Bot

from config import settings
from routers.commands import router as commands_router
from routers.form import router as form_router

bot_token = settings.BOT_TOKEN
dp = Dispatcher()

dp.include_routers(commands_router, form_router)


async def main() -> None:
    bot = Bot(token=bot_token)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
