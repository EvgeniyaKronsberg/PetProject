from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField
from wtforms.validators import DataRequired, Email


class LoginForm(FlaskForm):
    username = StringField('Имя пользователя', validators=[DataRequired()], render_kw={"class": "form-control"})
    password = PasswordField('Пароль', validators=[DataRequired()], render_kw={"class": "form-control"})
    email = EmailField('Адрес электронной почты', validators=[Email()], render_kw={"class": "form-control"})
    submit = SubmitField('Отправить', render_kw={'class': 'btn btn-primary'})