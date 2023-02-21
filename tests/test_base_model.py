import pytest
from lib.models.UserModel import UserModel
from lib.models.BaseModel import BaseModel
from .data_populator import populate_tables

@pytest.mark.parametrize("expected", ['test_user'])
def test_get(db, expected):
    populate_tables(['dashboard_users'])
    user = BaseModel()._get_('dashboard_users', 'id', 1)
    assert user['username'] == expected

def test_access_check():
    with pytest.raises(AttributeError):
        UserModel()._get_user()

def test_insert(db):
    columns = ['name', 'description', 'create_datetime', 'modify_datetime']
    values = ['Tester', 'Justa Test', 'NOW()', 'NOW()']
    id = BaseModel()._insert_('routine', columns, values)
    assert id == 1
