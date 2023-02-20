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
