from flask import Flask

from .private import internal
from .public import external

webapp = Flask(
    __name__, 
    template_folder='../frontend/templates',
    static_folder='../frontend/static'
)
webapp.secret_key = '93843hserj39sfsw3'
webapp.register_blueprint(external)
webapp.register_blueprint(internal)
