from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField
from wtforms import ValidationError, TextAreaField, DateField
from wtforms.validators import DataRequired, Length, Email, EqualTo, InputRequired, NumberRange
from models.user_user import User, UserDetails



class RegistrationForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired(), Length(min=2, max=50)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(min=2, max=50)])
    full_name = StringField('Full Name', validators=[DataRequired(), Length(min=2, max=50)])
    email = StringField('Email', validators=[DataRequired(), Email])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("The user with this email already exists!")


class PersonalInfo(FlaskForm):
    adress = StringField('Adress', validators=[DataRequired()])
    phone_number = StringField('Phone Number', validators=[DataRequired()])
    postal_code = StringField('Postal Code', validators=[DataRequired()])
    birth_date = StringField('Birth Date', validators=[DataRequired()])
    gender = StringField('Gender', validators=[DataRequired(), Length(min=1, max=1)])
    picture = FileField('Update profile picture', validators=[FileAllowed(['jpg', 'png'])])

    submit = SubmitField('Post')

    def validate_phone_number(self, phone_number):
        user = User.query.filter_by(phone_number=phone_number.data).first()
        if user:
            raise ValidationError("The user with this phone number already exists!")


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')



