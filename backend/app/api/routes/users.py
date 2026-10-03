from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status

from app.api.dependencies import get_user_controller
from app.controllers.user_controller import UserController
from app.schemas.user import UserCreate, UserResponse

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/", response_model=list[UserResponse])
def list_users(
    controller: Annotated[UserController, Depends(get_user_controller)],
) -> list[UserResponse]:
    return controller.list_users()

@router.get("/{user_id}", response_model=UserResponse)
def get_user(
    user_id: int,
    controller: Annotated[UserController, Depends(get_user_controller)],
) -> UserResponse:
    user = controller.get_user(user_id)
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user

@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(
    user_data: UserCreate,
    controller: Annotated[UserController, Depends(get_user_controller)],
) -> UserResponse:
    try:
        return controller.create_user(user_data)
    except ValueError as error:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(error),
        ) from error