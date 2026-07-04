from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from app.services.economy import get_or_create_user

router = Router()


@router.message(CommandStart())
async def start(message: Message):

    user = await get_or_create_user(message.from_user)

    await message.answer(
        f"""
👋 Привет, {user.first_name}!

Добро пожаловать в FamilyHub 🍉

Твой баланс:

🍉 {user.arbuz} арбузеров

Совсем скоро начнем играть!
"""
    )