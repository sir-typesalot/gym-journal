from flask import request, Blueprint

external = Blueprint('public', __name__)

@external.route('/')
def public():
    return "helllo public"

# Login
# Main Page
# Logout?
