from flask import Blueprint
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

from api.v1.views.search import *
from api.v1.views.hospital_service import *
from api.v1.views.hospitals import *
from api.v1.views.services import *
from api.v1.views.users import *
from api.v1.views.cities import *
from flask import Blueprint
from api.v1.views.orders import *
