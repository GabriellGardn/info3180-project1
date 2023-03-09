from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField
from wtforms.validators import InputRequired, DataRequired
from flask_wtf.file import FileField, FileRequired, FileAllowed


class NewPropertyForm(FlaskForm):

    title = StringField('Title', validators=[DataRequired()])
    bedrooms = StringField('Number of Bedrooms', validators=[DataRequired()])
    bathrooms = StringField('Number of Bathrooms', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    price = StringField('Price', validators=[DataRequired()])

    property_type = SelectField('Type', choices=[('House', 'House'), ('Apartment', 'Apartment')], validators=[DataRequired()])

    description = TextAreaField('Description')
    
    photo = FileField('Photo')