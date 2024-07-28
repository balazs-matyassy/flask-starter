from flask import Flask, render_template, g, redirect, url_for, request
from flask_wtf import CSRFProtect

import starter.core.context
import starter.core.persistence
import starter.core.security

import starter.modules.pages
import starter.modules.security
import starter.modules.users

from config import Config


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    csrf = CSRFProtect()
    csrf.init_app(app)

    starter.core.context.init_app(app)
    starter.core.persistence.init_app(app)
    starter.core.security.init_app(app)

    app.register_error_handler(400, lambda e: (render_template('errors/400.html'), 400))
    app.register_error_handler(401, __unauthorized)
    app.register_error_handler(404, lambda e: (render_template('errors/404.html'), 404))
    app.register_error_handler(500, lambda e: (render_template('errors/500.html'), 500))

    app.register_blueprint(starter.modules.pages.bp, url_prefix='/')
    app.register_blueprint(starter.modules.security.bp, url_prefix='/')
    app.register_blueprint(starter.modules.users.bp, url_prefix='/felhasznalok')

    return app


def __unauthorized(e):
    if not g.user:
        return redirect(url_for('security.login', redirect=request.path))

    return render_template('errors/401.html'), 401
