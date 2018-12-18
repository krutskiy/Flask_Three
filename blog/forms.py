from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from blog.models import User

class RegistrationForm(FlaskForm):
    username = StringField('Имя', 
                        validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    confirm_password = PasswordField('Подверждение пароля', 
                        validators=[DataRequired(), EqualTo('password')])
    remember = BooleanField('Забыли пароль?')
    submit = SubmitField('Регистрация')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Такой пользователь уже есть, выберите другого!')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Такая почта уже есть, выберите другую!')

class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember = BooleanField('Запомнить пароль?')
    submit = SubmitField('Вход')

class UpdateAccountForm(FlaskForm):
    username = StringField('Имя', 
                        validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    picture = FileField('Обновить фотографию', validators=[FileAllowed(['jpg', 'png'])])

    submit = SubmitField('Редактировать')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('Такой пользователь уже есть, выберите другого!')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('Такая почта уже есть, выберите другую!')

class PostForm(FlaskForm):
    title = StringField('Название', validators=[DataRequired()])
    content = TextAreaField('Содержимое', validators=[DataRequired()])
    submit = SubmitField('Записать')