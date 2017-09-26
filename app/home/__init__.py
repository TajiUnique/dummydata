__author__ = 'joe'

from flask import Blueprint

# create a Blueprint object and initialize it with a name
home = Blueprint('home', __name__)

from . import views
