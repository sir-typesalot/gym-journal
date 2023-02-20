
from lib.models.BaseModel import BaseModel

class RoutineModel(BaseModel):

    check_value = 'id'

    def __init__(self, routine_id=None):
        super().__init__()
        self.routine_info = {}
        if routine_id:
            self.set_routine(routine_id)

    def set_routine(self, routine_id):
        self.routine_id = routine_id
        self.name = self.get_attribute('name')

    @BaseModel.access_check(check_value)
    def _get_routine(self):
        if not self.routine_info:
            with self.db('dict') as cursor:
                cursor.execute("""
                    SELECT * FROM dashboard_users WHERE id = %s
                """, (self.routine_id, ))
                result = cursor.fetchone()
            self.routine_info = result if result else {}
        return self.routine_info
        
    @BaseModel.access_check(check_value)
    def get_attribute(self, attribute: str):
        return self._get_routine().get(attribute)

    def create_routine(self, name: str, description: str):
        with self.db() as cursor:
            cursor.execute("""
                INSERT INTO routine (name, description, create_datetime, modify_datetime) 
                VALUES (%s, %s, NOW(), NOW())
            """, (name, description))
            id = cursor.execute("SELECT MAX(id) FROM routine")
        self.set_user(id)
        return id
    

    
