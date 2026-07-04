import asyncio
import logging

from app.bot.bot import bot, dp
from app.handlers.start import router as start_router

logging.basicConfig(level=logging.INFO)

dp.include_router(start_router)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())