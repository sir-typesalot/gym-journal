import datetime
import json
from lib.models.BaseModel import BaseModel
from lib.models.RoutineLockModel import RoutineLockModel
from lib.models.RoutineModel import RoutineModel

class RoutineManager(BaseModel):
    
    def __init__(self, routine_id, user_id):
        super().__init__()
        self.routine_id = routine_id
        self.user_id = user_id
        self.has_lock = True if self.get_lock() else False

    def link_user(self, config: dict):
        # Add date to JSON data
        config['date_linked'] = datetime.now()

        columns = ['routine_id', 'user_id', 'config']
        values = [self.routine_id, self.user_id, json.dumps(config)]
        try:
            return self._insert_('routine_user_map', columns, values)
        except:
            raise RuntimeError("Trouble linking user to routine")

    def unlink_user(self):
        params = {
            'routine': self.routine_id,
            'user': self.user_id
        }
        conditions = ['routine_id = %(routine)s', 'user_id = %(user)s']
        delete = self._delete_('routine_user_map', conditions, params)
        return delete

    def lock(self):
        RoutineLockModel(self.routine_id).lock_routine(self.user_id)
        self.has_lock = True

    def unlock(self):
        RoutineLockModel(self.routine_id).release_lock()
        self.has_lock = False

    def get_lock(self):
        return RoutineLockModel(self.routine_id).get_lock()

    @classmethod
    def get(cls, id: int):
        return RoutineModel(routine_id=id).get_routine()
    
    @classmethod
    def create(cls, name: str, description: str):
        routine_id = RoutineModel().create_routine(name, description)
        return routine_id

    def delete(self):
        pass

    def update(self):
        pass

