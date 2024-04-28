from flask import jsonify, make_response  # type: ignore
from app.services.user_service import UserService


class UserController:
    @staticmethod
    def get_all_users():
        data = UserService.get_all_users()
        response = make_response(
            jsonify({"message": "List of users.", "data": data}), 200
        )
        return response

    @staticmethod
    def create_user():
        data = UserService.create_user()
        if data:
            response = make_response(jsonify({"message": "User created."}), 201)
            return response
        return make_response(jsonify({"message": "Something going wrong."}), 501)

    @staticmethod
    def get_user(id: int):
        data = UserService.get_user_by_id(id)
        response = make_response(
            jsonify({"message": "User information.", "data": data}), 200
        )
        return response
