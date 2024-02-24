from flask import Blueprint

from api.v1.views.state import init_state
from .index import *
from .state import *

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
init_app(app_views)
init_state(app_views)