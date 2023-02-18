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
    variables['routines'] = [
        {
            'name': 'Test Workout 1',
            'id': 1,
            'action': 'log',
            'notes': "Some example notes that might be in a workout template",
            'data': {
                'total_sets': 20,
                'exercises': ['Front Squat', 'Clean', 'RDL', 'Box Jumps']
            }
        },
        {
            'name': 'Test Workout 3',
            'id': 2,
            'action': 'log',
            'notes': "Some example notes that might be in a workout template",
            'data': {
                'total_sets': 15,
                'exercises': ['Bench Press', 'Push Press', 'Pushdown']
            }
        },
    ]
    variables['history'] = [
        {
            'name': 'Test Workout 1',
            'id': 1,
            'date': '02/14/2023',
            'notes': "Some example notes that might be in a workout template",
            'data': {
                'total_sets': 20,
                'exercises': ['Front Squat', 'Clean', 'RDL', 'Box Jumps']
            }
        },
    ]
    return render_template('dashboard.html', data=variables)

@internal.route('/routines/create-new', methods=['GET', 'POST'])
def create_routine():
    return render_template('new_routine.html', data=variables)
