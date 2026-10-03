from app.models.user import User
from app.schemas.user import UserCreate
from app.services.user_service import UserService


class UserController:
    def __init__(self, service: UserService) -> None:
        self._service = service

    def list_users(self) -> list[User]:
        return self._service.list_users()

    def get_user(self, user_id: int) -> User | None:
        return self._service.get_user(user_id)

    def create_user(self, user_data: UserCreate) -> User:
        return self._service.create_user(user_data)