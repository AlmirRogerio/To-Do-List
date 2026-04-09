from fastapi import HTTPException, status

from app.core.security import create_access_token, hash_password, verify_password
from app.repositories.user_repository import UserRepository
from app.dto.input.user import UserCreate, UserLogin
from app.dto.output.auth import TokenResponse
from app.dto.output.user import UserResponse


class AuthService:

    @staticmethod
    async def register(data: UserCreate) -> TokenResponse:
        if await UserRepository.find_by_email(data.email):
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Email já cadastrado")

        user = await UserRepository.create(
            name=data.name,
            email=data.email,
            password=hash_password(data.password),
        )
        token = create_access_token(user.id)
        return TokenResponse(
            access_token=token,
            user=UserResponse(id=user.id, name=user.name, email=user.email),
        )

    @staticmethod
    async def login(data: UserLogin) -> TokenResponse:
        user = await UserRepository.find_by_email(data.email)
        if not user or not verify_password(data.password, user.password):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciais inválidas")

        token = create_access_token(user.id)
        return TokenResponse(
            access_token=token,
            user=UserResponse(id=user.id, name=user.name, email=user.email),
        )
