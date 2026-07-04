from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

router = Router()


@router.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "👋 Привет!\n\n"
        "Я FamilyHubBot 🤖\n\n"
        "Совсем скоро я начну развлекать вашу семью:\n"
        "🧩 Загадки\n"
        "🎲 Игры\n"
        "😂 Шутки\n"
        "📸 Челленджи\n"
        "🎉 Викторины"
    )