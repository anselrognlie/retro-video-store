from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

db = SQLAlchemy()
migrate = Migrate()

def create_app(test_config=None):
    app = Flask(__name__)
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    if test_config is None:
        app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
            "SQLALCHEMY_DATABASE_URI")
    else:
        app.config["TESTING"] = True
        app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
            "SQLALCHEMY_DATABASE_URI_TEST")

    # app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@localhost:5432/video_store_development'
    # app.config['SQLALCHEMY_ECHO'] = True

    db.init_app(app)
    migrate.init_app(app, db)

    from app.models.customer import Customer
    from app.models.video import Video
    from app.models.rental import Rental

    from app.routes import customer
    from app.routes import rental
    app.register_blueprint(customer.bp)
    app.register_blueprint(rental.bp)

    return app
