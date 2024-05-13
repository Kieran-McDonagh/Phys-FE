from bson import ObjectId
from fastapi import HTTPException


class UserService:
    @staticmethod
    async def remove_user_from_all_friends_lists(collection, user_id):
        try:
            collection.update_many(
                {"friends": user_id}, {"$pull": {"friends": user_id}}
            )
        except Exception as e:
            print(f"An error occurred while removing user from friends lists: {e}")

    @staticmethod
    def apply_document_id_to_user(collection, document_id, user_id, attribute):
        try:
            updated_user = collection.find_one_and_update(
                {"_id": ObjectId(user_id)},
                {"$push": {attribute: str(document_id)}},
                return_document=True,
            )
            if updated_user is None:
                raise HTTPException(
                    status_code=404,
                    detail="User not found",
                )
        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=f"{e}",
            )

    @staticmethod
    def remove_document_id_from_user(collection, document_id, user_id, attribute):
        try:
            updated_user = collection.find_one_and_update(
                {"_id": ObjectId(user_id)},
                {"$pull": {attribute: str(document_id)}},
                return_document=True,
            )
            if updated_user is None:
                raise HTTPException(
                    status_code=404,
                    detail="User not found",
                )
        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=f"{e}",
            )
