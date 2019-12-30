from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FileField
from wtforms.validators import DataRequired
from flask_wtf.file import FileAllowed
from config_file_format import format_allowed


class AddSupermarket(FlaskForm):
    name = StringField('Supermarket Name', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    image = FileField('Image (please wait for 3 seconds)', validators=[DataRequired(), FileAllowed(format_allowed)])
    submit = SubmitField('Submit New Supermarket')
