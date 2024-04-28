from app.repositories.user_repository import UserRepository


class UserService:
    @staticmethod
    def get_all_users():
        return UserRepository.index()

    @staticmethod
    def get_user_by_id(id: int):
        return UserRepository.show(id)

    @staticmethod
    def create_user():
        return UserRepository.store()
