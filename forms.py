from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class registrationform(FlaskForm):
	username = StringField('username', validators=[DataRequired(), Length(min=2, max=50)])
	email = StringField('Email', validators=[DataRequired(), Email() ])
	password = PasswordField('Password', validators=[DataRequired()])
	confrim_password = PasswordField('Confrim Password', validators=[DataRequired(), EqualTo('password')])

	submit = SubmitField('SingUp')


class Loginform(FlaskForm):
	# username = StringField('username', validators=[DataRequired(), Lenght(min=2, max=50)])
	email = StringField('Email', validators=[DataRequired(), Email() ])
	password = PasswordField('Password', validators=[DataRequired()])
	remember = BooleanField('Remember Me')
	# confrim_password = PasswordField('Confrim Password', validators=[DataRequired(), EqualTo('password')])

	submit = SubmitField('Login')
