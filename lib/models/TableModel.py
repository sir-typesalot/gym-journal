from lib.models.BaseModel import BaseModel

class TableModel(BaseModel):

    def __init__(self, table: str):
        super().__init__()
        self.table = table
        self._table_data = None
        self.headers = None

    def create_table(self, keys: dict):
        """Create a pseudo table of a data subset in a DB table

        Args:
            keys (dict): Search values to create dataset
        """        
        self._table_data = self._get_(self.table, keys, fetch_all=True)
        self.headers = [x for x in self._table_data[0].keys()]

    @property
    def table_data(self):
        """Get the table data

        Returns:
            list: List of rows, represented as dicts
        """        
        return self._table_data

    @table_data.setter
    def set_data(self, value):
        """Set the table data

        Args:
            value (list): List of dicts, representing the new data
        """        
        self._table_data = value
        self._replace_rows()

    def _replace_rows(self):
        # Convert the table data into a list of tuples
        rows = [tuple(row.values()) for row in self.table_data]

        with self.db() as cursor:
            cursor.executemany(f"""
                REPLACE INTO {self.table}
                VALUES ({','.join(['%s' for x in self.headers])})
            """, rows)
    
    
