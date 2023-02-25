import pytest
from lib.models.UserModel import UserModel
from .data_populator import populate_tables

def test_create_user(db):
    user_id = UserModel().create(
        'test_user', 
        't@gmail.com', 
        'justapass'
    )
    assert user_id == 1

@pytest.mark.parametrize("user_id, expected", [
    ('9fe2c4e93f654fdbb24c02b15259716c', True),
    ('28374bd3hdb33738db', False)
])
def test_user_exists(db, user_id, expected):
    populate_tables(['dashboard_users'])
    exists = UserModel().user_exists(user_id)
    assert exists is expected

@pytest.mark.parametrize("user_id, expected", [
    ('9fe2c4e93f654fdbb24c02b15259716c', 'test_user'),
    ('28374bd3hdb33738db', None)
])
def test_get_user(db, user_id, expected):
    populate_tables(['dashboard_users'])
    user = UserModel().get({'user_id': user_id})
    if user:
        assert user.username == expected
    else: 
        assert user is None

@pytest.mark.parametrize("username,password,expected", [
    ('test_user','justapass', True), 
    ('foobar', 'blabla', False)
])
def test_authenticate_user(db, username, password, expected):
    populate_tables(['dashboard_users'])
    is_auth = UserModel().authenticate_user(username, password)
    assert is_auth is expected
    
