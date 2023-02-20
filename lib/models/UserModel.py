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
            with self.db('dict') as cursor:
                cursor.execute("""
                    SELECT * FROM dashboard_users WHERE user_id = %s
                """, (self.user_id, ))
                result = cursor.fetchone()
            self.user_info = result if result else {}
        return self.user_info
        
    @BaseModel.access_check(check_value)
    def get_attribute(self, attribute: str):
        return self._get_user().get(attribute)

    def create_user(self, username: str, email: str, pw: str, user_id: str):
        with self.db() as cursor:
            cursor.execute("""
                INSERT INTO dashboard_users (username, email, password_hash, user_id, create_datetime) 
                VALUES (%s, %s, %s, %s, NOW())
            """, (username, email, pw, user_id))
        self.set_user(user_id)
        return user_id
    
    # Change email
    # Change pw
