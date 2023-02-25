
from datetime import datetime
from lib.models.BaseModel import BaseModel
from lib.DataClasses import Routine, RoutineMap
from lib.models.UserModel import UserModel

class RoutineModel(BaseModel):

    def __init__(self):
        super().__init__()
        
    def create(self, name: str, description: bool):
        # Create dataclass and convert to dict
        routine = Routine(name, description, datetime.now(), datetime.now()).dict()
        try:
            # Derive columns and values from dict
            columns, values = self.split(routine)
            id = self.db.insert('routine', columns, values)
            return id
        except:
            # add logging at some point
            print("Unable to create routine")

    def exists(self, id: int):
        data = self.get({'id': id})
        return True if data else False

    def get(self, search_term: dict):
        routine = self.db.read('routine', search_term)
        if not routine:
            return None
        else:
            routine = self.sanitize(routine, Routine.headers())
            return Routine(**routine)
        
    def link_user(self, user_id: str, routine_id: int):
        user_exists = UserModel().user_exists(user_id)
        routine_exists = self.exists(id)
        if not user_exists or not routine_exists:
            raise LookupError(f"Can't link user: {user_exists} routine: {routine_exists}")
        else:
            user = UserModel().get({'user_id': user_id})
            routine = self.get({'id': routine_id})
            config = {
                'link_datetime': datetime.now()
            }
            routine_map = RoutineMap(routine.id, user.id, config)
            try:
                # Derive columns and values from dict
                columns, values = self.split(routine_map)
                id = self.db.insert('routine_user_map', columns, values)
                return id
            except:
                # add logging at some point
                print("Unable to link routine")

    def unlink_user(self):
        pass

    def delete(self):
        pass
