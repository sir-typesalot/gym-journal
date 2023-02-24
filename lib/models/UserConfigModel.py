from datetime import datetime
from lib.DataClasses import UserConfig
from .BaseModel import BaseModel

class UserConfigModel(BaseModel):

    def __init__(self):
        super().__init__()

    def create(self, user_id: int, param_name: str, param_value: str):
        # Create dataclass and convert to dict
        user_config = UserConfig(user_id, param_name, param_value, datetime.now()).dict()
        try:
            # Derive columns and values from dict
            columns, values = self.split(user_config)
            id = self.db.insert('user_configuration', columns, values)
            return id
        except:
            # add logging at some point
            print("Unable to add param to user")

    def get_all(self, search_term: dict):
        data = self.db.read('user_configuration', search_term, fetch_all=True)
        if not data:
            return None
        else:
            for row in data:
                config = self.sanitize(row, UserConfig.headers())
                row = UserConfig(**config)
            return data
    
    def get(self, search_term: dict):
        data = self.db.read('user_configuration', search_term)
        if not data:
            return None
        else:
            config = self.sanitize(data, UserConfig.headers())
            return UserConfig(**config)
    
    def update(self, user_id: int, param_name: str, param_value: str):
        setting = self.get({'user_id': user_id, 'param_name': param_name})
        setting.param_value = param_value
        if not setting:
            raise LookupError("Setting does not exist")
        else:
            values = setting.dict()
            condition = [f"user_id = {user_id}", f"param_name='{param_name}'"]
            id = self.db.update('user_configuration', values, condition)


    # Update setting
    # Delete setting
