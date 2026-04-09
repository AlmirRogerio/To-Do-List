from fastapi import APIRouter

from app.dto.input.user import UserCreate, UserLogin
from app.dto.output.auth import TokenResponse
from app.services.auth_service import AuthService

router = APIRouter()


@router.post("/register", response_model=TokenResponse, status_code=201)
async def register(data: UserCreate):
    return await AuthService.register(data)


@router.post("/login", response_model=TokenResponse)
async def login(data: UserLogin):
    return await AuthService.login(data)
