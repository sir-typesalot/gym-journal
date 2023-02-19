from lib.models.UserModel import UserModel
from .TestBase import db

def test_con(db):
    user_model = UserModel()
    assert UserModel().get_user() == {}
