from datetime import datetime
import uuid
import bcrypt
from lib.Scribe import Scribe
from lib.models.BaseModel import BaseModel
from lib.models.DataClassModel import User

class UserModel(BaseModel):

    def __init__(self):
        super().__init__()
        self.db = Scribe()
        self.id = None

    def create(self, username: str, email: str, pw: str):
        # Create user id and hash
        user_id = uuid.uuid4().hex
        password = self.create_password(pw)
        # Create dataclass and convert to dict
        user = User(username, email, password, datetime.now(), user_id).dict()
        try:
            # Derive columns and values from dict
            columns = list(user.keys())
            values = list(user.values())
            id = self.db.insert('dashboard_users', columns, values)
            return id
        except:
            # add logging at some point
            print("Unable to create user")

    def user_exists(self, user_id: str):
        data = self.db.read('dashboard_users', {'user_id': user_id})
        return True if data else False
    
    def get(self, search_term: dict):
        user = self.db.read('dashboard_users', search_term)
        if user:
            self.id = user['id']
            user = self.sanitize(user, User.headers())
            return User(**user)
        else:
            return None

    def create_password(self, pw: str):
        return bcrypt.hashpw(pw.encode('utf8'), bcrypt.gensalt())

    def check_password(self, hash: str, pw: str):
        return bcrypt.checkpw(pw.encode('utf8'), hash.encode('utf8'))

    def authenticate_user(self, username: str, password: str):
        user = self.get('dashboard_users', {'id': self.id})
        username_auth = user.get('username') == username
        password_auth = self.check_password(user['password_hash'], password)
        return password_auth and username_auth

    # Change email
    # Change pw
