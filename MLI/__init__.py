from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
from MLI.extension import db, login_manager
# from config import Config
from MLI.views.algorithm import algorithm
from MLI.views.dataset import dataset
from MLI.views.base import login
from MLI.views.preprocessing import preprocessing
from MLI.models import Admin, Algorithm, Dataset, Preprocessing


def register_extensions(app):
    db.init_app(app)
    login_manager.init_app(app)


def create_app():
    app = Flask('Machine Learning')

    # app.config.from_object(Config)

    register_extensions(app)
    app.register_blueprint(algorithm)
    app.register_blueprint(dataset)
    app.register_blueprint(login)
    app.register_blueprint(preprocessing)

    return app


if __name__ == "__main__":
    app = create_app()
    # db.create_all()
    app.run()
