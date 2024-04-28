# config.py


class Config:
    SQLALCHEMY_DATABASE_URI = (
        "mysql+mysqlconnector://root:root%40root@localhost:3306/flask_crud"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
