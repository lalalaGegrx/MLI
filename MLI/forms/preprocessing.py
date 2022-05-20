from flask_wtf import FlaskForm
from wtforms import BooleanField, SubmitField


class PreForm(FlaskForm):
    Standardization = BooleanField('Standardization')
    Nothing = BooleanField('Nothing')
    Nothing_1 = BooleanField('Nothing')
    submit = SubmitField()
