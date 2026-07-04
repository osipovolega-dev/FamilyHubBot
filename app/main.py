import asyncio
import logging

from app.bot.bot import bot, dp
from app.database.db import init_db
from app.handlers.start import router as start_router

from app.handlers.register import router as register_router

logging.basicConfig(level=logging.INFO)

dp.include_router(start_router)
dp.include_router(register_router)


async def main():
    logging.info("Создание базы данных...")
    await init_db()
    logging.info("База данных готова.")

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())