from flask import Flask  # type: ignore
from flask_sqlalchemy import SQLAlchemy  # type: ignore
from config import Config

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    from app.routes.user_routes import user_blueprint

    app.register_blueprint(user_blueprint)

    return app
