import logging
from lib.Scribe import Scribe

logging.basicConfig(level = logging.INFO)

class BaseModel(object):

    def __init__(self):
        self.logger = logging.getLogger("base_logger")
        self.db = Scribe()
    
    def sanitize(self, data: dict, headers: list):
        """Sanitize raw data before passing into dataclass

        Args:
            data (dict): Raw data to process
            headers (list): Headers of dataclass

        Returns:
            dict: Key->Values that conform to the dataclass
        """        
        return {k: data[k] for k in headers}
    
    def split(self, entity: dict):
        """Extract columns and values from an entity dict

        Args:
            entity (dict): Dict to extract

        Returns:
            (tuple): Columns and Values in list forms
        """        
        columns = list(entity.keys())
        values = list(entity.values())
        return columns, values
