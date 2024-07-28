from flask import current_app

from starter.core import local_now

__timestamp = None


def init_app(app):
    app.before_request(__update_context)

    app.jinja_env.globals['weekday'] = __weekday


def __update_context():
    global __timestamp

    now = local_now()

    current_app.jinja_env.globals['date'] = now.date()
    current_app.jinja_env.globals['time'] = now.time()
    current_app.jinja_env.globals['datetime'] = now


def __weekday(date):
    if date.weekday() == 0:
        return 'hétfő'
    elif date.weekday() == 1:
        return 'kedd'
    elif date.weekday() == 2:
        return 'szerda'
    elif date.weekday() == 3:
        return 'csütörtök'
    elif date.weekday() == 4:
        return 'péntek'
    elif date.weekday() == 5:
        return 'szombat'
    elif date.weekday() == 6:
        return 'vasárnap'

    return None
