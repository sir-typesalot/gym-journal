from datetime import datetime
from lib.DataClasses import RoutineLock
from lib.models.BaseModel import BaseModel

class RoutineLockModel(BaseModel):

    def __init__(self, routine_id):
        super().__init__()
        self.routine_id = routine_id
        self.is_locked = False
    
    def get_lock(self):
        param = {
            'routine_id': self.routine_id
        }
        lock = self.db.read('routine_edit_lock', param)
        if not lock:
            self.is_locked = False
            return None
        else:
            self.is_locked = True
            lock = self.sanitize(lock, RoutineLock.headers())
            return RoutineLock(**lock)
        
    def lock(self, user_id: int):
        exists = self.get_lock()
        if exists:
            print("Lock already exists")
            self.is_locked = True
            return exists
        else:
            lock = RoutineLock(self.routine_id, user_id, datetime.now()).dict()
            columns, values = self.split(lock)
            self.db.insert('routine_edit_lock', columns, values)
            self.is_locked = True
            return lock

    def release_lock(self):
        params = {'routine_id': self.routine_id}
        conditions = ["routine_id = %(routine_id)s"]
        result = self.db.drop('routine_edit_lock', params, conditions)
        return True if result else False
    