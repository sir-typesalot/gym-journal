from .TestBase import test_db

# content of test_sample.py
def inc(x):
    return x + 1

def test_answer():
    assert inc(3) == 4

def test_db_con(test_db):
    with test_db() as cursor:
        cursor.execute("SHOW TABLES")
        data = cursor.fetchall()

    assert data == []
