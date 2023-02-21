import logging
from app.config import Config
from lib.db import DB

logging.basicConfig(level = logging.INFO)

class BaseModel(object):

    check_value = None

    def __init__(self):
        self.db = DB(db=Config.SCHEMA).db_connect
        self.logger = logging.getLogger("base_logger")
    
    def access_check(value):
        def decorator(function):
            def wrapper(self, *args, **kwargs):
                if hasattr(self, value):
                    return function(self, *args, **kwargs)
                else:
                    raise AttributeError(f"Cannot access class method without {value} set")
            return wrapper
        return decorator
    
    def _get_(self, table: str, column: str, value: str):
        """Get data from table in database

        Args:
            table (str): Table to retrieve from
            column (str): Column to search by
            value (str): Value to search

        Returns:
            (dict): Result
        """
        with self.db('dict') as cursor:
            cursor.execute(f"SELECT * FROM {table} WHERE {column} = %s", (value, ))
            return cursor.fetchone()
        
    def _insert_(self, table: str, columns: list, values: list):
        """Method to perform simple INSERT operation

        Args:
            table (str): Table to insert into
            column (str): Columns to add data for
            value (str): Data values
        """
        with self.db() as cursor:
            cursor.execute(f"""
                INSERT INTO {table} ({','.join(columns)})
                VALUES ({','.join(['%s' for x in values])})
            """, tuple(values))
            
            return cursor.getlastrowid()
