import pytest
from lib.db import DB
from app.config import Config
from lib.models.BaseModel import BaseModel

@pytest.fixture
def test_db():
    Config.SCHEMA = '_test_db'
    yield DB(Config.SCHEMA).db_connect

@pytest.fixture
def db():
    Config.SCHEMA = '_test_db'
