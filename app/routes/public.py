from flask import request, Blueprint, render_template

external = Blueprint('public', __name__)

variables = {
    'title': 'Home',
    'footer_text': 'Gym-Journal'
}

@external.route('/')
def public():
    return render_template('home.html', vars=variables)

# Login
# Main Page
# Logout?
