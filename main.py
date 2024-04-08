from flask import Flask  # type: ignore
from src.controllers.todo_controller import todo_bp
from src.controllers.user_controller import user_bp

app = Flask(__name__)

app.register_blueprint(todo_bp, url_prefix="/todos")
app.register_blueprint(user_bp, url_prefix="/users")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
