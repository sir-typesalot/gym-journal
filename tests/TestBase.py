import pytest
from lib.db import DB

@pytest.fixture
def test_db():
    yield DB('_test_db').db_connect
