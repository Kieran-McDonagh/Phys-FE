from backend.models.user_models.new_user import NewUser


class UserBuilder:
    def __init__(self):
        user = NewUser()
        user._id = None
        user.name = None
        user.email = None
        self._entity = user
        
    def with_id(self, user_id):
        self._entity._id = user_id
        return self

    def with_name(self, user_name):
        self._entity.name = user_name
        return self

    def with_email(self, user_email):
        self._entity.email = user_email
        return self

    def build(self):
        return self._entity
