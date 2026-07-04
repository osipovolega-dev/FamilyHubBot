from sqlalchemy import select

from app.database.db import SessionLocal
from app.database.models import User


async def get_or_create_user(telegram_user):
    async with SessionLocal() as session:

        result = await session.execute(
            select(User).where(
                User.telegram_id == telegram_user.id
            )
        )

        user = result.scalar_one_or_none()

        if user:
            return user

        user = User(
            telegram_id=telegram_user.id,
            username=telegram_user.username,
            first_name=telegram_user.first_name,
            arbuz=0,
            wins=0,
            games=0,
        )

        session.add(user)
        await session.commit()

        return user