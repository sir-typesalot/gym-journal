from lib.models.BaseModel import BaseModel

class TableModel(BaseModel):

    def __init__(self, table: str):
        super().__init__()
        self.table = table
        self._table_data = None

    def create_table(self, keys: dict):
        self._table_data = self._get_(self.table, keys, fetch_all=True)

    @property
    def table_data(self):
        return self._table_data

    @table_data.setter
    def set_data(self, value):
        self._table_data = value
        self._replace_rows()

    def _replace_rows(self):
        # Use REPLACE INTO to replace the columns
        pass
    
