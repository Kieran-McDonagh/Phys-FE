from backend.repositories.user_repository import UserRepository


class UserController:
    @staticmethod
    async def get_all_users(name=None):
        users = await UserRepository.fetch_all_users(name)
        return users

    @staticmethod
    async def get_by_id(id):
        user = await UserRepository.fetch_by_id(id)
        return user

    @staticmethod
    async def post_user(user):
        new_user = await UserRepository.add_user(user)
        return new_user

    @staticmethod
    async def update_user(id, update):
        updated_user = await UserRepository.edit_user(id, update)
        return updated_user

    @staticmethod
    async def delete_user(id):
        deleted_user = await UserRepository.remove_user(id)
        return deleted_user
