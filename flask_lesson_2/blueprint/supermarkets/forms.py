from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FileField
from wtforms.validators import DataRequired
from flask_wtf.file import FileAllowed


class AddSupermarket(FlaskForm):
    name = StringField('Supermarket Name', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    image = FileField('Image', validators=[DataRequired(), FileAllowed(['jpeg', 'jpg', 'png', 'gif', 'bmp'])])
    submit = SubmitField('Submit New Supermarket')
