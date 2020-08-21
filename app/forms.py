from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, \
    TextAreaField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, \
    Length

#flask_wtf autogenerates forms if u give it info on form fields

class MemberForm(FlaskForm):
    firstName =  StringField('First Name', validators=[DataRequired()])
    lastName =  StringField('Last Name', validators=[DataRequired()])
    buisName =  StringField('Name of Business', validators=[DataRequired()])
    buisAddress =  StringField('Address of Business', validators=[DataRequired()])
    email = StringField('Email Address', validators=[DataRequired(), Email()])
    phonePrimary =  StringField('Primary Phone Number', validators=[DataRequired()])
    phoneBuis=  StringField('Business Phone Number', validators=[DataRequired()])
    website =  StringField('Website', validators=[DataRequired()])
    submit = SubmitField('Sign In')
