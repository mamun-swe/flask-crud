from src.repositories.todo_repository import TodoRepository


class TodoService:
    @staticmethod
    def create():
        return TodoRepository.create()

    @staticmethod
    def get_all():
        return TodoRepository.getAll()

    @staticmethod
    def get_by_id():
        return TodoRepository.getByid()

    @staticmethod
    def update():
        return TodoRepository.update()

    @staticmethod
    def destroy():
        return TodoRepository.destroy()
