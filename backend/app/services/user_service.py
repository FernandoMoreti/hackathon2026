from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate


class UserService:
    def __init__(self, repository: UserRepository) -> None:
        self._repository = repository

    def list_users(self) -> list[User]:
        return self._repository.get_all()

    def get_user(self, user_id: int) -> User | None:
        return self._repository.get_by_id(user_id)

    def create_user(self, user_data: UserCreate) -> User:
        if self._repository.get_by_email(user_data.email) is not None:
            raise ValueError("Email already registered")

        user = User(name=user_data.name, email=user_data.email)
        return self._repository.create(user)