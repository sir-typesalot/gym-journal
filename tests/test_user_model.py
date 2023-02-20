import pytest
from lib.models.UserModel import UserModel
from .data_populator import populate_tables

@pytest.mark.parametrize("expected", ['test_user'])
def test_get_user(db, expected):
    populate_tables(['dashboard_users'])
    user = UserModel('9fe2c4e93f654fdbb24c02b15259716c')._get_user()
    assert user['username'] == expected

@pytest.mark.parametrize("username,password,expected", [('test_user','justapass', True), ('foobar', 'blabla', False)])
def test_authenticate_user(db, username, password, expected):
    populate_tables(['dashboard_users'])
    is_auth = UserModel('9fe2c4e93f654fdbb24c02b15259716c').authenticate_user(username, password)
    assert is_auth is expected

@pytest.mark.parametrize("user_id,expected", [('9fe2c4e93f654fdbb24c02b15259716c', 1), ('abd342', None)])
def test_get_user_id(db, user_id, expected):
    populate_tables(['dashboard_users'])
    id = UserModel(user_id).get_id()
    assert id == expected

@pytest.mark.parametrize("user_id,expected", [('9fe2c4e93f654fdbb24c02b15259716c', 'test_user'), ('abd342', None)])
def test_get_username(db, user_id, expected):
    populate_tables(['dashboard_users'])
    username = UserModel(user_id=user_id).get_username()
    assert username == expected
