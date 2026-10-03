from datetime import date

from pydantic import BaseModel, ConfigDict


class OrderCreate(BaseModel):
    description: str
    order_date: date
    file_name: str
    content_type: str
    file_content: bytes


class OrderResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    description: str
    order_date: date
    file_name: str
    content_type: str