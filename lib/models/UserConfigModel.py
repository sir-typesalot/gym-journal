from datetime import datetime
from lib.DataClasses import UserConfig
from .BaseModel import BaseModel

class UserConfigModel(BaseModel):

    def __init__(self, user_id: int):
        super().__init__()
        self.user_id = user_id

    def create(self, param_name: str, param_value: str):
        # Create dataclass and convert to dict
        user_config = UserConfig(self.user_id, param_name, param_value, datetime.now()).dict()
        try:
            # Derive columns and values from dict
            columns, values = self.split(user_config)
            id = self.db.insert('user_configuration', columns, values)
            return id
        except:
            # add logging at some point
            print("Unable to add param to user")

    def get_all(self):
        params = {
            'user_id': self.user_id
        }
        data = self.db.read('user_configuration', params, fetch_all=True)
        if not data:
            return None
        else:
            for row in data:
                config = self.sanitize(row, UserConfig.headers())
                row = UserConfig(**config)
            return data
    
    def get(self, param_name: str):
        params = {
            'user_id': self.user_id,
            'param_name': param_name
        }
        data = self.db.read('user_configuration', params)
        if not data:
            return None
        else:
            config = self.sanitize(data, UserConfig.headers())
            return UserConfig(**config)
    
    def update(self, param_name: str, param_value: str):
        setting = self.get({'user_id': self.user_id, 'param_name': param_name})
        setting.param_value = param_value
        if not setting:
            raise LookupError("Setting does not exist")
        else:
            values = setting.dict()
            condition = [f"user_id = {self.user_id}", f"param_name='{param_name}'"]
            id = self.db.update('user_configuration', values, condition)
            return id

    def delete(self, param_name: str):
        params = {
            'user_id': self.user_id,
            'param_name': param_name
        }
        conditions = ["user_id = %(user_id)s", "param_name = %(param_name)s"]
        result = self.db.drop('user_configuration', params, conditions)
        return True if result else False
