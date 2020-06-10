from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

class CompanyResearchForm(FlaskForm):
    company_name = StringField('Company Name', validators=[DataRequired()
        ,Length(min=2, max=20)])

    company_website = StringField('Company Website', validators=[DataRequired()
        ,Length(min=2, max=15)])

    company_desc = StringField('Company Description', validators=[DataRequired()
        ,Length(min=2, max=50)])
    
    

    # password = PasswordField('Password', validators=[DataRequired()])

    # confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])

    submit = SubmitField('Add Record')

    