from fastapi import APIRouter
from backend.models.user_models.new_user import NewUser
from backend.controllers.user_controller import UserController

router = APIRouter()

# CREATE
@router.post("/user")
async def post_user(user: NewUser):
    return await UserController.post_user(user)

# READ
@router.get("/user")
async def get_all_users():
    return await UserController.get_all_users()

@router.get("/user/{id}")
async def get_user_by_id(id: str):
    return await UserController.get_user_by_id(id)

# UPDATE
@router.put("/user/{id}")
async def update_user(id: str, user_update: NewUser):
    return await UserController.update_user_by_id(id, user_update.dict())

# DELETE
@router.delete("/user/{id}")
async def delete_user(id: str):
    return await UserController.delete_user_by_id(id)