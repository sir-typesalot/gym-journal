import os
import logging
import contextlib
import mysql.connector
from dotenv import load_dotenv
logging.basicConfig(level = logging.INFO)

@contextlib.contextmanager
def db_connect(cur_type=None):
    load_dotenv()
    config = {
        "host": os.environ.get('DB_HOST'),
        "user": os.environ.get('DB_USER'),
        "passwd": os.environ.get('DB_PASSWORD'),
        "database": 'workout_log'
    }

    cnx = mysql.connector.MySQLConnection(**config)

    if cur_type == 'dict':
        cursor = cnx.cursor(dictionary=True)
    else: 
        cursor = cnx.cursor()

    try:
        yield cursor
    finally:
        cnx.commit()
        cursor.close()
        cnx.close()
