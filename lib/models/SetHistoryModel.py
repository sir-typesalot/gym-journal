from datetime import datetime
from lib.models.BaseModel import BaseModel
from lib.DataClasses import SetHistory
from lib.models.ExerciseModel import ExerciseModel
from lib.models.SetModel import SetModel

class SetHistoryModel(BaseModel):

    def __init__(self, set_id: int):
        super().__init__()
        self.set_id = set_id

    def create(self, count: int, load: float):
        ex_set = SetModel().get({'routine_id': self.set_id})
        if not ex_set:
            raise LookupError(f"Can't add history for set: {self.set_id}")
        else:
            exercise_set = SetHistory(self.set_id, ex_set.unit, count, load, datetime.now())
            columns, values = self.split(exercise_set)
            id = self.db.insert('set_history', columns, values)
            return id
        
    def get(self, search_term):
        ex_set = self.db.read('set_history', search_term)
        if not ex_set:
            return None
        else:
            ex_set = self.sanitize(ex_set, SetHistory.headers())
            return SetHistory(**ex_set)
        
    def modify(self, set: SetHistory):
        columns, values = self.split(set.dict())
        self.db.replace('exercise_sets', columns, values)

    def delete(self, id: int):
        values = {
            'id': id
        }
        conditions = ["id = %(id)s"]
        self.db.drop('set_history', values, conditions)
