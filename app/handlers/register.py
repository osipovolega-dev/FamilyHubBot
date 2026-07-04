from aiogram import Router
from aiogram.types import Message

from app.services.economy import get_or_create_user

router = Router()


@router.message()
async def register_user(message: Message):

    if not message.from_user:
        return

    await get_or_create_user(message.from_user)