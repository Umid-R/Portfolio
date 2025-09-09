from flask_wtf import FlaskForm
from wtforms import StringField, EmailField , SubmitField
from wtforms.validators import DataRequired

class MyForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email =  EmailField('Email', validators=[DataRequired()])
    phone = StringField('Phone Number', validators=[DataRequired()])
    message = StringField('Message',validators=[DataRequired()])
    submit=SubmitField(label='Message')