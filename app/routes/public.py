from flask import request, Blueprint, render_template

external = Blueprint('public', __name__)

variables = {
    'title': 'Home',
    'footer_text': 'Gym-Journal',
    'cache': 1
}

@external.route('/', methods=['GET'])
def public():
    return render_template('home.html', vars=variables)

@external.route('/login', methods=['GET', 'POST'])
def login():
    variables['title'] = "Login"
    return render_template('login.html', vars=variables)

@external.route('/signup', methods=['GET', 'POST'])
def sign_up():
    variables['title'] = "Sign Up"
    return render_template('signup.html', vars=variables)
