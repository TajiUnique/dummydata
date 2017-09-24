# import render_templates
__author__ = 'joe'
from flask import Blueprint

# blueprint object creation and initialization
auth = Blueprint('auth', __name__)

from . import views