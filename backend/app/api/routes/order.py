from datetime import date
from pathlib import Path
from typing import Annotated
from xml.etree import ElementTree

from fastapi import APIRouter, Depends, File, Form, HTTPException, UploadFile, status

from app.api.dependencies import get_order_controller
from app.controllers.order_controller import OrderController
from app.schemas.order import OrderCreate, OrderResponse

router = APIRouter(prefix="/orders", tags=["Orders"])
MAX_FILE_SIZE = 10 * 1024 * 1024


@router.get("/", response_model=list[OrderResponse])
def list_orders(
    controller: Annotated[OrderController, Depends(get_order_controller)],
) -> list[OrderResponse]:
    return controller.list_orders()


@router.get("/{order_id}", response_model=OrderResponse)
def get_order(
    order_id: int,
    controller: Annotated[OrderController, Depends(get_order_controller)],
) -> OrderResponse:
    order = controller.get_order(order_id)
    if order is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order not found")
    return order


@router.post("/", response_model=list[OrderResponse], status_code=status.HTTP_201_CREATED)
def create_orders(
    files: Annotated[list[UploadFile], File()],
    option: Annotated[str, Form()],
    order_date: Annotated[date, Form(alias="date")],
    controller: Annotated[OrderController, Depends(get_order_controller)],
) -> list[OrderResponse]:
    return controller.create_orders(files, option, order_date)