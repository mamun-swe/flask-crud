from src.repositories.user_repository import UserRepository


class UserService:
    @staticmethod
    def create():
        return UserRepository.create()

    @staticmethod
    def get_all():
        return UserRepository.getAll()

    @staticmethod
    def get_by_id():
        return UserRepository.getByid()

    @staticmethod
    def update():
        return UserRepository.update()

    @staticmethod
    def destroy():
        return UserRepository.destroy()
