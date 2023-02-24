import pytest
from lib.models.ExerciseModel import ExerciseModel
from .data_populator import populate_tables

@pytest.mark.parametrize("name, expected", [
    ('Chest Press', 1)
])
def test_create_new(db, name, expected):
    exists = ExerciseModel().create_new(name, False, False, {})
    assert exists is expected

def test_create_new_error(db):
    populate_tables(['exercises'])
    with pytest.raises(NameError):
        ExerciseModel().create_new('Bench Press', False, False, {})
