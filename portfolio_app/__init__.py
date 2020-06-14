from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail

db = SQLAlchemy()
migrate = Migrate()
mail = Mail()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    from portfolio_app.main import bp
    app.register_blueprint(bp)

    db.init_app(app)
    migrate.init_app(app, db)
    mail.init_app(app)

    return app