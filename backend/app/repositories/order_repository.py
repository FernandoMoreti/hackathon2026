from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.order import Order


class OrderRepository:
    def __init__(self, session: Session) -> None:
        self._session = session

    def get_all(self) -> list[Order]:
        return list(self._session.scalars(select(Order).order_by(Order.id)))

    def get_by_id(self, order_id: int) -> Order | None:
        return self._session.get(Order, order_id)

    def create(self, order: Order) -> Order:
        return