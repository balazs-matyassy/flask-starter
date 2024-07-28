from urllib.parse import urlsplit

from flask import g, redirect, url_for, session, flash, request, render_template
from sqlalchemy.exc import SQLAlchemyError

from starter.core.security.decorators import is_granted
from starter.modules.security import bp
from starter.modules.security.forms import (LoginForm, ChangePasswordForm)
from starter.modules.users.repositories import UserRepository


@bp.route('/bejelentkezes', methods=('GET', 'POST'))
def login():
    if g.user:
        return redirect(url_for('pages.home'))

    form = LoginForm()

    if form.validate_on_submit():
        user = UserRepository.find_by_username(form.username.data)

        if user and user.check_password(form.password.data):
            session['user_id'] = user.id
            flash('Bejelentkezés sikeres.')

            if (request.args.get('redirect')
                    and not urlsplit(request.args.get('redirect')).netloc):
                return redirect(request.args.get('redirect'))

            return redirect(url_for('pages.home'))
        else:
            flash('Hibás felhasználónév vagy jelszó.')

    return render_template('security/login.html', form=form)


@bp.route('/kijelentkezes')
def logout():
    session.clear()
    flash('Kijelentkezés sikeres.')

    return redirect(url_for('pages.home'))


@bp.route('/jelszo-megvaltoztatasa', methods=('GET', 'POST'))
@is_granted('IS_AUTHENTICATED_FULLY')
def change_password():
    user = g.user
    form = ChangePasswordForm()

    if form.validate_on_submit():
        form.populate_obj(user)

        try:
            UserRepository.save(user)
            flash('Jelszó megváltoztatva.')

            return redirect(url_for('security.profile'))
        except SQLAlchemyError:
            flash('Hiba történt a jelszó megváltoztatása közben!')

    return render_template('security/change_password.html', form=form, user=user)
