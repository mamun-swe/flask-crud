from flask import jsonify, make_response  # type: ignore
from app.services.user_service import UserService


class UserController:
    @staticmethod
    def index():
        data = UserService.index()
        response = make_response(
            jsonify({"message": "List of users.", "data": data}), 200
        )
        return response

    @staticmethod
    def store():
        data = UserService.store()
        if data:
            response = make_response(jsonify({"message": "User created."}), 201)
            return response
        return make_response(jsonify({"message": "Something going wrong."}), 501)

    @staticmethod
    def show(id: int):
        data = UserService.show(id)
        response = make_response(
            jsonify({"message": "User information.", "data": data}), 200
        )
        return response

    @staticmethod
    def destroy(id: int):
        data = UserService.destroy(id)
        if data == True:
            response = make_response(
                jsonify({"message": "User information.", "data": "User deleted"}), 200
            )
            return response

        response = make_response(
            jsonify({"message": "User information.", "data": "User not found."}), 404
        )
        return response
