from .BaseModel import BaseModel
from werkzeug.security import generate_password_hash, check_password_hash

class UserModel(BaseModel):

    def __init__(self, username=None, user_id=None):
        super().__init__()
        self.username = username
        self.is_created = True if username else False

    def get_user(self, username):

        with self.db('dict') as cursor:
            cursor.execute("""
                SELECT * FROM dashboard_users WHERE username = %s
            """, (username, ))
            result = cursor.fetchone()
        
        if not result:
            return {}

        return result
        
    def create_new_user(self, username, password, email):

        if self.user_exists(username):
            self.is_created = True
            self.username = username
            return {}, 300
        
        password_hash = generate_password_hash(password=password)

        with self.db() as cursor:
            cursor.execute("""
                INSERT INTO dashboard_users (username,password,email,date_created,last_updated) 
                VALUES (%s, %s, %s, NOW(), NOW())
            """, (username, password_hash, email))
        
        self.username = username
        result = self.get_user_id()

        status = 200 if result else 500
        return result, status

    def user_exists(self, username):
        # Check to see if user already exists in the DB
        with self.db('dict') as cursor:
            cursor.execute("SELECT * FROM dashboard_users WHERE username = %s", (username, ))
            result = cursor.fetchall()

        return True if result else False

    def authenticate_user(self, username, password):
        user = self.get_user(username)

        username_auth = user['username'] == username
        password_auth = check_password_hash(user['password'], password)

        return password_auth and username_auth

    def get_user_id(self, username=None):
        
        if not username:
            username = self.username
        # Get user id
        with self.db('dict') as cursor:
            cursor.execute("SELECT user_id from dashboard_users WHERE username = %s", (username,))
            result = cursor.fetchone()

        return result['user_id']

    def get_username(self, id=None):
        
        if not id:
            id = self.user_id
        # Get user id
        with self.db('dict') as cursor:
            print(id)
            cursor.execute("SELECT username from dashboard_users WHERE user_id = %d", (id,))
            result = cursor.fetchone()

        return result['username']
