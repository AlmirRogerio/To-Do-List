import os


SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key-change-in-production")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24

DATABASE_URL = os.getenv("DATABASE_URL", "mysql://todouser:todopass@db:3306/todolist")

CORS_ORIGINS = [
    os.getenv("CORS_ORIGIN", "http://localhost:8080"),
]
