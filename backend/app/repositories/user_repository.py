from app.models import User


class UserRepository:

    @staticmethod
    async def find_by_email(email: str) -> User | None:
        return await User.get_or_none(email=email)

    @staticmethod
    async def find_by_id(user_id: int) -> User | None:
        return await User.get_or_none(id=user_id)

    @staticmethod
    async def create(name: str, email: str, password: str) -> User:
        return await User.create(name=name, email=email, password=password)
