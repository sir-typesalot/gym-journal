import os
import contextlib
import mysql.connector
from dotenv import load_dotenv

class DB(object):
    
    def __init__(self, db='gym_journal'):
        self.db = db

    @contextlib.contextmanager
    def db_connect(self, cur_type=None):
        load_dotenv()
        config = {
            "host": os.environ.get('DB_HOST'),
            "user": os.environ.get('DB_USER'),
            "passwd": os.environ.get('DB_PASSWORD'),
            "database": self.db
        }

        cnx = mysql.connector.MySQLConnection(**config)

        if cur_type == 'dict':
            cursor = cnx.cursor(dictionary=True, buffered=True)
        else:
            cursor = cnx.cursor(buffered=True)

        try:
            yield cursor
        finally:
            cnx.commit()
            cursor.close()
            cnx.close()
