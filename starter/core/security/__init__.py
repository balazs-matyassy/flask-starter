from flask import g, session

from starter.core.security.utils import check_granted, check_owner_or_granted
from starter.modules.users.repositories import UserRepository


def init_app(app):
    app.before_request(__load_current_user)

    app.jinja_env.globals['is_granted'] = check_granted
    app.jinja_env.globals['is_owner_or_granted'] = check_owner_or_granted


def __load_current_user():
    if not session.get('user_id'):
        g.user = None
    else:
        g.user = UserRepository.find_by_id(session.get('user_id'))
