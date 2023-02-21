
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
            result = self._get_('routine', 'id', self.routine_id)
            self.routine_info = result if result else {}
        return self.routine_info
        
    @BaseModel.access_check(check_value)
    def get_attribute(self, attribute: str):
        return self._get_routine().get(attribute)

    def create_routine(self, name: str, description: str):
        columns = ['name', 'description', 'create_datetime', 'modify_datetime']
        values = [name, description, 'NOW()', 'NOW()']
        try:
            self._insert_('routine', columns, values)
            with self.db() as cursor:
                cursor.execute("SELECT MAX(id) from routine")
                routine_id = cursor.fetchone()
            return routine_id
        except:
            print("Trouble creatng routine")
    