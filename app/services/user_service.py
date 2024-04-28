from app.repositories.user_repository import UserRepository


class UserService:
    @staticmethod
    def index():
        return UserRepository.index()

    @staticmethod
    def store():
        return UserRepository.store()

    @staticmethod
    def show(id: int):
        return UserRepository.show(id)

    @staticmethod
    def destroy(id: int):
        return UserRepository.destroy(id)
