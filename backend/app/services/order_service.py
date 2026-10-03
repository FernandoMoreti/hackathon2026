from app.models.order import Order
from app.repositories.order_repository import OrderRepository
from app.schemas.order import OrderCreate


class OrderService:
    def __init__(self, repository: OrderRepository) -> None:
        self._repository = repository

    def list_orders(self) -> list[Order]:
        return self._repository.get_all()

    def get_order(self, order_id: int) -> Order | None:
        return self._repository.get_by_id(order_id)

    def create_order(self, order_data: OrderCreate) -> Order:
        return self._repository.create(order_data)

