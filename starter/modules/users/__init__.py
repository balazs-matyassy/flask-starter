from flask import Blueprint

bp = Blueprint('users', __name__)

from starter.modules.users import routes
