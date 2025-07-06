import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.enums import ParseMode
from aiogram.client.bot import DefaultBotProperties
from bot.config import load_config
from bot.handlers import register_all_handlers
from bot.database.notes_db import create_db

logging.basicConfig(level=logging.INFO)

async def main():
    config = load_config()

    bot = Bot(token=config.bot_token.get_secret_value(),
        default=DefaultBotProperties(parse_mode=ParseMode.HTML,))

    dp = Dispatcher(storage=MemoryStorage())

    register_all_handlers(dp)

    await create_db()

    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.info("Stop.")