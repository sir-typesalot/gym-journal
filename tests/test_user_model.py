import pytest
from lib.models.UserModel import UserModel
from .data_populator import populate_tables

@pytest.mark.parametrize("expected", ['test_user'])
def test_get_user(db, expected):
    populate_tables(['dashboard_users'])
    user = UserModel('9fe2c4e93f654fdbb24c02b15259716c')._get_user()
    assert user['username'] == expected

# @pytest.mark.parametrize("username,password,expected", [('test_user','justapass', True), ('foobar', 'blabla', False)])
# def test_authenticate_user(db, username, password, expected):
#     populate_tables(['dashboard_users'])
#     is_auth = UserModel('9fe2c4e93f654fdbb24c02b15259716c').authenticate_user(username, password)
#     assert is_auth is expected

@pytest.mark.parametrize("user_id,attribute,expected", [
    ('9fe2c4e93f654fdbb24c02b15259716c', 'username', 'test_user'),
    ('abd342', 'username', None),
    ('9fe2c4e93f654fdbb24c02b15259716c', 'id', 1),
    ('abd342', 'id', None)
])
def test_get_attribute(db, user_id, attribute, expected):
    populate_tables(['dashboard_users'])
    result = UserModel(user_id=user_id).get_attribute(attribute=attribute)
    assert result == expected

def test_create_user(db):
    user_id = UserModel().create_user(
        'test_user', 
        't@gmail.com', 
        '$2y$04$Lfxl0lAeEvh1/ek62Z81Yuaq7h.Qa2oGxh9l7uItscmkMGaDIon.C',
        '9fe2c4e93f654fdbb24c02b15259717d'
    )
    assert user_id == 1
