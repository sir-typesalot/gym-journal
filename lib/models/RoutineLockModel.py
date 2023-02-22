
from lib.models.BaseModel import BaseModel

class RoutineModel(BaseModel):

    def __init__(self, routine_id):
        super().__init__()
        self.routine_id = routine_id

    def get_lock(self):
        details = self._get_('routine_edit_lock', {'routine_id': self.routine_id})
        return details if details else {}

    def lock_routine(self, user_id: int):
        columns = ['routine_id', 'user_id', 'start_datetime']
        values = [self.routine_id, user_id, 'NOW()']
        try:
            self._insert_('routine_edit_lock', columns, values)
            return self.routine_id
        except:
            print(f"Trouble creatng lock for {self.routine_id}")

    def release_lock(self):
        with self.db() as cursor:
            cursor.execute("DELETE FROM routine_edit_lock WHERE routine_id = %s", (self.routine_id, ))
            success = cursor.statement
        return True if success else False
    