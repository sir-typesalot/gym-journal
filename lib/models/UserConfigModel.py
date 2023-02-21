from .BaseModel import BaseModel

class UserConfigModel(BaseModel):

    def __init__(self, user_id):
        super().__init__()
        self.user_settings = {}
        if not user_id:
            raise ValueError("Must have a user ID")
        self.set_user(user_id)

    def set_user(self, user_id):
        self.user_id = user_id

    def _get_settings(self, param=None):
        if not self.user_settings:
            result = self._get_('user_configuration', 'user_id', self.user_id, fetch_all=True)
            self.user_settings = result if result else {}
        return self.user_settings

    def get_setting(self, attribute: str):
        return self._get_settings.get(attribute)

    def add_setting(self, param_name: str, param_value: str):
        columns = ['user_id', 'parameter_name', 'parameter_value', 'modify_datetime']
        values = [self.user_id, param_name, param_value, 'NOW()']
        try:
            id = self._insert_('user_configuration', columns, values)
            return id
        except:
            print("Trouble adding user")

    # Update setting
    # Delete setting
