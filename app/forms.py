
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired, Optional
from wtforms.widgets import TextArea
from flask_wtf.file import FileField, FileAllowed, FileRequired
from werkzeug.utils import secure_filename

class PropertyForm(FlaskForm):
    title=StringField('Property Title',validators=[DataRequired()])
    number_of_bedrooms=StringField('No. of Rooms', validators=[DataRequired()])
    number_of_bathrooms=StringField('No. of Bathrooms', validators=[DataRequired()])
    location=StringField('Location', validators=[DataRequired()])
    price=StringField('Price', validators=[DataRequired()])
    types=SelectField('Property Type', choices = [('House', 'House'), ('Apartment', 'Apartment')], validators=[Optional()])
    description=StringField('Description', widget=TextArea(), validators=[DataRequired()])
    photo=FileField('Photo',validators=[FileRequired(), FileAllowed(['jpg','png'], 'Please Upload Images Only!')])