
from flask import flash, redirect, url_for, request, render_template, abort
from sqlalchemy.exc import SQLAlchemyError

from starter.core.persistence.decorators import param
from starter.core.security.decorators import is_granted
from starter.modules.users import bp
from starter.modules.users.forms import CreateUserForm, EditUserForm
from starter.modules.users.models import User
from starter.modules.users.repositories import UserRepository


@bp.route('/')
@is_granted('ROLE_ADMIN')
def list_all():
    if 'search' in request.args:
        users = UserRepository.find_all_by_username_like(request.args['search'])
    else:
        users = UserRepository.find_all()

    return render_template('users/list.html', users=users)


@bp.route('/letrehozas', methods=('GET', 'POST'))
@is_granted('ROLE_ADMIN')
def create():
    user = User()
    form = CreateUserForm(obj=user)

    if form.validate_on_submit():
        form.populate_obj(user)

        try:
            UserRepository.save(user)
            flash('Felhasználó létrehozva.')

            return redirect(url_for('users.list_all'))
        except SQLAlchemyError as err:
            if 'duplicate' in str(err).lower():
                flash('A megadott felhasználónévvel már létezik felhasználó!')
            else:
                flash('Hiba történt az új felhasználó létrehozása során!')

    return render_template('users/create.html', form=form)


@bp.route('/szerkesztes/<username>', methods=('GET', 'POST'))
@is_granted('ROLE_ADMIN')
@param('user', UserRepository.find_by_username, 'username')
def edit(user):
    form = EditUserForm(obj=user)

    if form.validate_on_submit():
        form.populate_obj(user)

        try:
            UserRepository.save(user)
            flash('Felhasználó mentve.')

            return redirect(url_for('users.edit', username=user.username))
        except SQLAlchemyError as err:
            if 'duplicate' in str(err).lower():
                flash('A megadott felhasználónévvel már létezik felhasználó!')
            else:
                flash('Hiba történt a felhasználó mentése során!')

    return render_template('users/edit.html', form=form)


@bp.route('/torles/<username>', methods=('POST',))
@is_granted('ROLE_ADMIN')
@param('user', UserRepository.find_by_username, 'username')
def delete(user):
    try:
        UserRepository.delete(user)
        flash('Felhasználó törölve.')
    except SQLAlchemyError:
        flash('Hiba történt a felhasználó törlése közben!')

    return redirect(url_for('users.list_all'))
