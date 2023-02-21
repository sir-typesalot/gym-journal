import pytest
from lib.db import DB
from app.config import Config

def get_db():
    Config.SCHEMA = '_test_db'
    db = DB(Config.SCHEMA).db_connect
    return db()
    
@pytest.fixture
def db():
    Config.SCHEMA = '_test_db'
    yield
    tables = ['dashboard_users', 'routine_edit_lock', 'routine', 'exercises']
    with get_db() as cursor:
        cursor.execute("SET FOREIGN_KEY_CHECKS = 0")
        for table in tables:
            cursor.execute(f"TRUNCATE TABLE {table}")

