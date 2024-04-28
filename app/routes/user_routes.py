from flask import Blueprint  # type: ignore
from app.controllers.user_controller import UserController

user_blueprint = Blueprint("user", __name__)


@user_blueprint.route("/users", methods=["GET"])
def index():
    return UserController.index()


@user_blueprint.route("/users", methods=["POST"])
def store():
    return UserController.store()


@user_blueprint.route("/users/<int:id>", methods=["GET"])
def show(id):
    return UserController.show(id)


@user_blueprint.route("/users/<int:id>", methods=["DELETE"])
def destroy(id):
    return UserController.destroy(id)
