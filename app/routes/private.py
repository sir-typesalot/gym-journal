from flask import request, Blueprint

internal = Blueprint('private', __name__)

@internal.route('/private')
def private():
    return "helllo"
