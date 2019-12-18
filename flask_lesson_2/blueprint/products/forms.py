from flask_wtf import FlaskForm
from decimal import Decimal
from wtforms import StringField, SubmitField, FileField, FloatField
from wtforms.validators import DataRequired, NumberRange
from flask_wtf.file import FileAllowed


class AddProduct(FlaskForm):
    name = StringField('Product Name', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    price = FloatField('Price', validators=[DataRequired(), NumberRange(min=0.01)])
    image = FileField('Image', validators=[DataRequired(), FileAllowed(['jpeg', 'jpg', 'png', 'gif', 'bmp'])])
    submit = SubmitField('Submit New Product')
