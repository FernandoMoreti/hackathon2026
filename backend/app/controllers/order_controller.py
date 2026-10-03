from app.models.order import Order
from app.schemas.order import OrderCreate
from app.services.order_service import OrderService

from app.utils.reader_xml import read_xml_file

class OrderController:
    def __init__(self, service: OrderService) -> None:
        self._service = service

    def list_orders(self) -> list[Order]:
        return self._service.list_orders()

    def get_order(self, order_id: int) -> Order | None:
        return self._service.get_order(order_id)

    def create_order(self, order_data: OrderCreate) -> Order:
        return self._service.create_order(order_data)

    def create_orders(self, orders_data: list[OrderCreate], option: str, order_date) -> list[Order]:
        json_data = read_xml_file(orders_data)
        return self._service.create_order(json_data, option, order_date)