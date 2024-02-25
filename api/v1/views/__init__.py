from flask import Blueprint
from .index import *
from .cities import *

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')


init_app(app_views)