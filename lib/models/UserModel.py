from .BaseModel import BaseModel

class UserModel(BaseModel):

    check_value = 'user_id'

    def __init__(self, user_id=None):
        super().__init__()
        self.user_info = {}
        if user_id:
            self.set_user(user_id)

    def set_user(self, user_id):
        self.user_id = user_id
        self.id = self.get_attribute('id')
        self.username = self.get_attribute('username')

    @BaseModel.access_check(check_value)
    def _get_user(self):
        if not self.user_info:
            result = self._get_('dashboard_users', 'user_id', self.user_id)
            self.user_info = result if result else {}
        return self.user_info
        
    @BaseModel.access_check(check_value)
    def get_attribute(self, attribute: str):
        return self._get_user().get(attribute)

    def create_user(self, username: str, email: str, pw: str, user_id: str):
        columns = ['username', 'email', 'password_hash', 'user_id', 'create_datetime']
        values = [username, email, pw, user_id, 'NOW()']
        try:
            id = self._insert_('dashboard_users', columns, values)
            self.set_user(user_id)
            return id
        except:
            print("Trouble adding user")

    # Change email
    # Change pw
