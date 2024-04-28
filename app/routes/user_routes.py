from flask import Blueprint  # type: ignore
from app.controllers.user_controller import UserController

user_blueprint = Blueprint("user", __name__)


@user_blueprint.route("/users", methods=["GET"])
def get_users():
    return UserController.get_all_users()


@user_blueprint.route("/users", methods=["POST"])
def create_user():
    return UserController.create_user()


@user_blueprint.route("/users/<int:id>", methods=["GET"])
def get_user(id):
    return UserController.get_user(id)
