from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, InputRequired

class MyForm(FlaskForm):
    name = StringField('name', validators=[DataRequired(), InputRequired()])
    email = EmailField('email', validators=[DataRequired(), InputRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired(), InputRequired(), Length(min=8, max=30)])
    submit = SubmitField('login')