from flask_wtf import FlaskForm
from wtforms.fields.simple import SubmitField, PasswordField, StringField
from wtforms.validators import InputRequired, Length, Optional
from wtforms_sqlalchemy.fields import QuerySelectField

from starter.modules.users.repositories import RoleRepository


class UserFormMixin:
    username = StringField('Felhasználónév', validators=[
        InputRequired('Hiányzik az érték!'),
        Length(max=180, message='Túl hosszú érték!')
    ])
    role = QuerySelectField('Szerepkör', query_factory=RoleRepository.find_all, get_label='name')
    first_name = StringField('Keresztnév', validators=[
        Optional(),
        Length(max=180, message='Túl hosszú érték!')
    ], filters=[lambda x: x or None])
    last_name = StringField('Vezetéknév', validators=[
        Optional(),
        Length(max=180, message='Túl hosszú érték!')
    ], filters=[lambda x: x or None])
    submit = SubmitField('Mentés')


class CreateUserForm(FlaskForm, UserFormMixin):
    password = PasswordField('Jelszó', validators=(
        InputRequired(message='Hiányzik az érték!'),
    ))


class EditUserForm(FlaskForm, UserFormMixin):
    password = PasswordField('Password', validators=(
        Optional(),
    ))
