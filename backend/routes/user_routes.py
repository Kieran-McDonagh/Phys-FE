from fastapi import APIRouter, Query
from backend.controllers.user_controller import UserController
from backend.models.user_models.new_user import NewUser

router = APIRouter()


@router.get("/users", status_code=200)
async def get_all_users(name: str = Query(None)):
    return await UserController.get_all_users(name)


@router.get("/users/{id}", status_code=200)
async def get_user_by_id(id: str):
    return await UserController.get_by_id(id)


@router.post("/users", status_code=201)
async def post_user(user: NewUser):
    return await UserController.post_user(user)


@router.put("/users/{id}", status_code=201)
async def update_user_by_id(id: str, updated_user: NewUser):
    return await UserController.update_user(id, updated_user)


@router.delete("/users/{id}", status_code=200)
async def delete_user_by_id(id: str):
    return await UserController.delete_user(id)
