from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from app.services.content_loader import random_riddle

router = Router()


@router.message(Command("riddle"))
async def riddle(message: Message):
    item = random_riddle()

    await message.answer(
        f"🧩 <b>Загадка дня</b>\n\n"
        f"{item['question']}\n\n"
        f"Ответ: <tg-spoiler>{item['answer']}</tg-spoiler>",
        parse_mode="HTML"
    )