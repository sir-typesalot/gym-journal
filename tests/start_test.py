from .TestBase import test_db

def test_db_con(test_db):
    with test_db('dict') as cursor:
        cursor.execute("SHOW TABLES")
        data = cursor.fetchall()

    assert len(data) == 8
