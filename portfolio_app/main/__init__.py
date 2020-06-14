from flask import Blueprint

bp = Blueprint("main", __name__)

from portfolio_app.main import views