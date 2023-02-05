import logging
from lib.db import DB

logging.basicConfig(level = logging.INFO)

class BaseModel(object):

    def __init__(self):
        self.db = DB().db_connect
        self.logger = logging.getLogger("base_logger")
