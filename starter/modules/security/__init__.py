from flask import Blueprint

bp = Blueprint('security', __name__)

from starter.modules.security import routes
