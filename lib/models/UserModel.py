from datetime import datetime
import uuid
import bcrypt
from lib.models.BaseModel import BaseModel
from lib.DataClasses import User

class UserModel(BaseModel):

    def __init__(self):
        super().__init__()
        self.id = None

    def create(self, username: str, email: str, pw: str):
        # Create user id and hash
        user_id = uuid.uuid4().hex
        password = self.create_password(pw)
        # Create dataclass and convert to dict
        user = User(username, email, password, datetime.now(), user_id).dict()
        try:
            # Derive columns and values from dict
            columns, values = self.split(user)
            id = self.db.insert('dashboard_users', columns, values)
            return id
        except:
            # add logging at some point
            print("Unable to create user")

    def user_exists(self, user_id: str):
        data = self.get({'user_id': user_id})
        return True if data else False

    def get(self, search_term: dict):
        user = self.db.read('dashboard_users', search_term)
        if not user:
            return None
        else:
            self.id = user['id']
            user = self.sanitize(user, User.headers())
            return User(**user)
            
    def create_password(self, pw: str):
        return bcrypt.hashpw(pw.encode('utf8'), bcrypt.gensalt())

    def check_password(self, hash: str, pw: str):
        return bcrypt.checkpw(pw.encode('utf8'), hash.encode('utf8'))

    def authenticate_user(self, username: str, password: str):
        user = self.get({'username': username})
        if not user:
            return False
        else:
            username_auth = user.username == username
            password_auth = self.check_password(user.password_hash, password)
            return password_auth and username_auth

    # Change email
    # Change pw
