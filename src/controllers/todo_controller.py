from flask import Blueprint, jsonify  # type: ignore
from src.services.todo_service import TodoService

todo_bp = Blueprint("todo", __name__)


@todo_bp.route("/", methods=["GET"])
def index():
    data = TodoService.get_all()
    return jsonify({"message": data})


@todo_bp.route("/", methods=["POST"])
def store():
    data = TodoService.create()
    return jsonify({"message": data})


@todo_bp.route("/<int:id>", methods=["GET"])
def show(id):
    data = TodoService.get_by_id()
    return jsonify({"id": id, "message": data})


@todo_bp.route("/<int:id>", methods=["PUT"])
def update(id):
    data = TodoService.update()
    return jsonify({"id": id, "message": data})


@todo_bp.route("/<int:id>", methods=["DELETE"])
def destroy(id):
    data = TodoService.destroy()
    return jsonify({"id": id, "message": data})
