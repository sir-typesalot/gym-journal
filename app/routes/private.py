from flask import render_template, Blueprint

internal = Blueprint('private', __name__)

variables = {
    'title': 'Home',
    'footer_text': 'Gym-Journal',
    'cache': 1
}

@internal.route('/private')
def private():
    return "helllo"

@internal.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', vars=variables)
