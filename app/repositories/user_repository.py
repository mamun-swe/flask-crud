from app.models.user import User
from app import db


class UserRepository:
    @staticmethod
    def index():
        users = User.query.all()
        # Serialize each user object to a dictionary
        serialized_users = [user.serialize() for user in users]
        return serialized_users

    @staticmethod
    def store():
        new_user = User(name="Abdullah Al Mamun", email="mamun.swe.277@gmail.com")
        db.session.add(new_user)
        db.session.commit()
        return new_user.id

    @staticmethod
    def show(id: int):
        user = User.query.get(id)
        if user:
            serialized_user = user.serialize()
            return serialized_user
        return None

    @staticmethod
    def destroy(id: int):
        user = User.query.get(id)
        if user:
            db.session.delete(user)
            db.session.commit()
            return True
        return False
