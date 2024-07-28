from flask_wtf import FlaskForm
from wtforms.fields.simple import PasswordField, SubmitField, StringField
from wtforms.validators import InputRequired, Length, EqualTo


class LoginForm(FlaskForm):
    username = StringField('Felhasználónév', validators=(
        InputRequired(message='Hiányzik az érték!'),
    ))
    password = PasswordField('Jelszó', validators=(
        InputRequired(message='Hiányzik az érték!'),
    ))
    submit = SubmitField('Bejelentkezés')


class ChangePasswordForm(FlaskForm):
    password = PasswordField('Jelszó', validators=(
        InputRequired(message='Hiányzik az érték!'),
        Length(min=10, message='Túl rövid jelszó!')
    ))
    confirm_password = PasswordField('Jelszó megerősítése', validators=(
        InputRequired(message='Hiányzik az érték!'),
        EqualTo('password', message='A jelszavak nem egyeznek meg!')
    ))
    submit = SubmitField('Mentés')
