from flask import render_template

from starter.modules.pages import bp


@bp.route('/')
def home():
    return render_template('base.html')
