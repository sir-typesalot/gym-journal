import logging
from app.config import Config
from lib.db import DB
 
class Scribe(object):

    def __init__(self):
        self.db = DB(db=Config.SCHEMA).db_connect
        self.logger = logging.getLogger("scribe")
 
    def read(self, table: str, values: dict, fetch_all=False):
        """Simple GET operation to fetch from table in DB

        Args:
            table (str): Table name
            values (dict): A map of the columns->values to search for
            fetch_all (bool, optional): Whether to fetch all results of one. Defaults to False.

        Returns:
            if fetch_all:
                list: List of rows, represented as dicts 
            else:
                dict: Singular row result
        """            
        with self.db('dict') as cursor:
            cursor.execute(f"""
                SELECT * FROM {table} 
                WHERE {' AND '.join([f'{x} = %s' for x in values.keys()])}
            """, tuple(values.values()))
            data = cursor.fetchall()
        
        if data and not fetch_all:
            return data[0]
        else:
            return data
        
    def insert(self, table: str, columns: list, values: list):
        """Method to perform simple INSERT operation

        Args:
            table (str): Table to insert into
            column (list): Columns to add data for
            value (list): Data values
        
        Returns:
            int: Last row id of an auto increment column
        """       
        with self.db() as cursor:
            cursor.execute(f"""
                INSERT INTO {table} ({','.join(columns)})
                VALUES ({','.join(['%s' for x in values])})
            """, tuple(values))
            
            return cursor.getlastrowid()

    def update(self, table: str, new_values: dict, condition: list):
        """Simple update method to aid in generic operations

        Args:
            table (str): Name of target table
            values (dict): A map of the columns->values to set to
            condition (list): The conditions to check for

        Returns:
            str: The executed statement
        """        
        with self.db() as cursor:
            cursor.execute(f"""
                UPDATE {table}
                SET {','.join([f'{x} = %s' for x,y in new_values.items()])}
                WHERE {' AND '.join(condition)}
            """, tuple(new_values.values()))
            return cursor._executed
        
    def drop(self, table: str, condition_values: dict, condition: list):
        """Simple delete method for basic operations

        Args:
            table (str): Target table name
            condition (list): List of conditions to fulfill
            values (dict): Map of values to apply to the conditions

        Returns:
            str: Executed query
        """        
        with self.db() as cursor:
            cursor.execute(f"""
                DELETE {table}
                WHERE {' AND '.join(condition)}
            """, condition_values)
            return cursor._executed
        
    def custom_query(self, query: str, params: dict):
        """Method in case extra functionality is required beyond simple CRUD

        Args:
            query (str): Query to run
            params (dict): Params used in the query

        Returns:
            _type_: _description_
        """        
        with self.db() as cursor:
            cursor.execute(query, params)
        return 0

