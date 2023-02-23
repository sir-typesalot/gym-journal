from functools import lru_cache
import logging
from app.config import Config
from lib.db import DB

logging.basicConfig(level = logging.INFO)

class BaseModel(object):

    def __init__(self):
        self.logger = logging.getLogger("base_logger")
    
    def sanitize(self, data: dict, headers: list):
        """Sanitize raw data before passing into dataclass

        Args:
            data (dict): Raw data to process
            headers (list): Headers of dataclass

        Returns:
            dict: Key->Values that conform to the dataclass
        """        
        return {k: data[k] for k in headers}
