# Add any form classes for Flask-WTF here
from wtforms import StringField, IntegerField, EmailField, TextAreaField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Email
from flask_wtf.file import FileAllowed, FileRequired,FileField

class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = StringField('password', validators=[DataRequired()])

class MovieForm(FlaskForm):
    m_title = StringField('Movie Title', validators=[DataRequired()])
    m_desc = TextAreaField('Movie Description', validators=[DataRequired()])
    m_poster = FileField('Movie Poster', validators=[FileRequired(), FileAllowed('jpg', 'jpeg', 'png', 'gif'), 'Images Only!'])