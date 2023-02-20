from .BaseModel import BaseModel
from typing import Optional
import uuid
import bcrypt

class UserModel(BaseModel):

    def __init__(self, user_id: str):
        super().__init__()
        self.user_id = user_id
        self.id = self.get_id()

    def _get_user(self):

        with self.db('dict') as cursor:
            cursor.execute("""
                SELECT * FROM dashboard_users WHERE user_id = %s
            """, (self.user_id, ))
            result = cursor.fetchone()

        return result if result else {}

    def authenticate_user(self, username: str, password: str):
        user = self._get_user()

        username_auth = user.get('username') == username
        password_auth = self.check_password(user['password_hash'], password)

        return password_auth and username_auth

    def get_id(self):
        return self._get_user().get('id')

    def get_username(self):
        return self._get_user().get('username')

    def check_password(self, hash: str, pw: str):
        return bcrypt.checkpw(pw.encode('utf8'), hash.encode('utf8'))
