from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, InputRequired, EqualTo


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')


class ResetForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    current_password = PasswordField('Current Password', validators=[DataRequired()])
    new_password = PasswordField('New Password', validators=[DataRequired()])
    password_confirm = PasswordField('Confirm New Password',
                                     validators=[InputRequired(),
                                                 EqualTo('new_password', message='Passwords must match')])
    submit = SubmitField('Reset Password')
