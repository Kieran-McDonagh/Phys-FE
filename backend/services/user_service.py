class UserService:
    @staticmethod
    async def remove_user_from_all_friends_lists(collection, user_id):
        try:
            collection.update_many(
                {"friends": user_id}, {"$pull": {"friends": user_id}}
            )
        except Exception as e:
            print(f"An error occurred while removing user from friends lists: {e}")