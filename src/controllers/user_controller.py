from flask import Blueprint, jsonify  # type: ignore
from src.services.user_service import UserService

user_bp = Blueprint("user", __name__)


@user_bp.route("/", methods=["GET"])
def index():
    data = UserService.get_all()
    return jsonify({"message": data})


@user_bp.route("/", methods=["POST"])
def store():
    data = UserService.create()
    return jsonify({"message": data})


@user_bp.route("/<int:id>", methods=["GET"])
def show(id):
    data = UserService.get_by_id()
    return jsonify({"id": id, "message": data})


@user_bp.route("/<int:id>", methods=["PUT"])
def update(id):
    data = UserService.update()
    return jsonify({"id": id, "message": data})


@user_bp.route("/<int:id>", methods=["DELETE"])
def destroy(id):
    data = UserService.destroy()
    return jsonify({"id": id, "message": data})
