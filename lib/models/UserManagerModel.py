import uuid

import bcrypt
from lib.models.BaseModel import BaseModel
from .UserModel import UserModel

class UserManagerModel(BaseModel):
    
    def create_new_user(self, username, password, email):
        if self.user_exists(username):
            raise AssertionError(f"User {username} already exists")
        
        password_hash = self.create_password(password)
        user_id = uuid.uuid4().hex

        with self.db() as cursor:
            cursor.execute("""
                INSERT INTO dashboard_users (username, email, password_hash, create_datetime) 
                VALUES (%s, %s, %s, %s NOW())
            """, (username, email, password_hash, user_id))
        return user_id
    
    def user_exists(self, username):
        # Check to see if user already exists in the DB
        with self.db('dict') as cursor:
            cursor.execute("SELECT * FROM dashboard_users WHERE username = %s", (username, ))
            result = cursor.fetchall()

        return True if result else False
    
    def create_password(self, pw):
        return bcrypt.hashpw(pw.encode('utf8'), bcrypt.gensalt())
