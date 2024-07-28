from flask import Blueprint

bp = Blueprint('pages', __name__)

from starter.modules.pages import routes
