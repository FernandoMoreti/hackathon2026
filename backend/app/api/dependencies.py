from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session

from app.controllers.order_controller import OrderController
from app.controllers.user_controller import UserController
from app.db.dependencies import get_db_session
from app.repositories.order_repository import OrderRepository
from app.repositories.user_repository import UserRepository
from app.services.order_service import OrderService
from app.services.user_service import UserService


def get_user_controller(
    session: Annotated[Session, Depends(get_db_session)],
) -> UserController:
    repository = UserRepository(session)
    service = UserService(repository)
    return UserController(service)

def get_order_controller(
    session: Annotated[Session, Depends(get_db_session)],
) -> OrderController:
    repository = OrderRepository(session)
    service = OrderService(repository)
    return OrderController(service)