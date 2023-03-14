from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField
from wtforms.validators import InputRequired, DataRequired
from flask_wtf.file import FileField, FileRequired, FileAllowed


class NewPropertyForm(FlaskForm):

    title = StringField('Property Title', validators=[DataRequired()])
    description = TextAreaField('Description')
    bedrooms = StringField('No. of Rooms', validators=[DataRequired()])
    bathrooms = StringField('No. of Bathrooms', validators=[DataRequired()])
    price = StringField('Price', validators=[DataRequired()])
    property_type = SelectField('Type', choices=[('House', 'House'), ('Apartment', 'Apartment')], validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    photo = FileField('Browse')