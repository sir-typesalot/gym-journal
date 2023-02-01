import logging
from lib.db import db_connect

logging.basicConfig(level = logging.INFO)

class BaseModel(object):

    def __init__(self):
        self.db = db_connect
        self.logger = logging.getLogger("base_logger")
