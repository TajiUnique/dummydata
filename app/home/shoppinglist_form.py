__author__ = 'joe'

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, ValidationError, IntegerField
from wtforms.validators import DataRequired


class ShoppingList(FlaskForm):

    n