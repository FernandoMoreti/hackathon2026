from contextlib import asynccontextmanager
from collections.abc import AsyncIterator

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes.users import router as users_router
from app.api.routes.order import router as order_router
from app.db.config import settings
from app.db.database import database


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncIterator[None]:
  database.create_schema()
  yield
  database.dispose()


app = FastAPI(
  title=settings.app_name,
  description="API modular para gerenciamento de usuários.",
  version="1.0.0",
  lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Libera o seu frontend Next.js
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos os métodos (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Permite todos os headers
)

app.include_router(users_router)
app.include_router(order_router)

@app.get("/", tags=["Health"])
def health_check() -> dict[str, str]:
  return {"message": "API funcionando. Acesse /docs para ver a documentação."}
