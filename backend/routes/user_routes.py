from fastapi import APIRouter, Query, Depends
from backend.controllers.user_controller import UserController
from backend.models.user_models.new_user import NewUser
from backend.security.authentication import Authenticate


router = APIRouter()


@router.get(
    "/users",
    status_code=200,
    dependencies=[Depends(Authenticate.get_current_active_user)],
)
async def get_all_users(username: str = Query(None)):
    return await UserController.get_all_users(username)


@router.get(
    "/users/{id}",
    status_code=200,
    dependencies=[Depends(Authenticate.get_current_active_user)],
)
async def get_user_by_id(id: str):
    return await UserController.get_by_id(id)


@router.post("/users", status_code=201)
async def post_user(user: NewUser):
    return await UserController.post_user(user)


@router.put(
    "/users/{id}",
    status_code=201,
    dependencies=[Depends(Authenticate.get_current_active_user)],
)
async def update_user_by_id(id: str, updated_user: NewUser):
    return await UserController.update_user(id, updated_user)


@router.delete(
    "/users/{id}",
    status_code=200,
    dependencies=[Depends(Authenticate.get_current_active_user)],
)
async def delete_user_by_id(id: str):
    return await UserController.delete_user(id)
