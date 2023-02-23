import uuid
import bcrypt
from lib.models.BaseModel import BaseModel
from models.UserModel import UserModel

class UserManager(BaseModel):
    
    def create_new_user(self, username, password, email):
        if self.user_exists(username):
            raise AssertionError(f"User {username} already exists")
        
        password_hash = self.create_password(password)
        user_id = uuid.uuid4().hex

        user = UserModel().create_user(username, email, password_hash, user_id)
        return True if user else False
        
    def user_exists(self, user_id: str):
        user = UserModel(user_id)._get_user()
        return True if user else False
    
    def create_password(self, pw: str):
        return bcrypt.hashpw(pw.encode('utf8'), bcrypt.gensalt())
    
    def authenticate_user(self, username: str, password: str):
        user = self._get_user()
        username_auth = user.get('username') == username
        password_auth = self.check_password(user['password_hash'], password)
        return password_auth and username_auth
    
    def check_password(self, hash: str, pw: str):
        return bcrypt.checkpw(pw.encode('utf8'), hash.encode('utf8'))


# TODO: Implement a session management system
# Either in this manager or a dedicated one
