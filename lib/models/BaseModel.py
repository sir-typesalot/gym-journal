import logging
from app.config import Config
from lib.db import DB

logging.basicConfig(level = logging.INFO)

class BaseModel(object):

    def __init__(self):
        self.db = DB(db=Config.SCHEMA).db_connect
        self.logger = logging.getLogger("base_logger")
