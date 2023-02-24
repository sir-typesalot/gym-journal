from lib.models.BaseModel import BaseModel
from lib.DataClasses import ExerciseSet
from lib.models.ExerciseModel import ExerciseModel
from lib.models.RoutineModel import RoutineModel

class SetModel(BaseModel):

    def __init__(self, routine_id: int):
        super().__init__()
        self.routine_id = routine_id

    def create(self, exercise_id: int, display_order: int, unit: int, count: int, details: dict):
        routine = RoutineModel().get({'routine_id': self.routine_id})
        exercise = ExerciseModel().get({'id': exercise_id})
        if not routine or not exercise:
            raise LookupError(f"Can't add set routine: {self.routine_id} exercise: {exercise_id}")
        else:
            exercise_set = ExerciseSet(exercise.id, routine.id, display_order, unit, count, details)
            columns, values = self.split(exercise_set)
            id = self.db.insert('exercise_sets', columns, values)
            return id
        
    def get(self, search_term):
        ex_set = self.db.read('exercise_sets', search_term)
        if not ex_set:
            return None
        else:
            ex_set = self.sanitize(ex_set, ExerciseSet.headers())
            return ExerciseSet(**ex_set)
        
    def modify(self, set: ExerciseSet):
        columns, values = self.split(set.dict())
        self.db.replace('exercise_sets', columns, values)

    def delete(self, set_id: int):
        values = {
            'routine_id': self.routine_id,
            'set_id': set_id
        }
        conditions = ["routine_id = %(routine_id)s","id = %(set_id)s"]
        self.db.drop('exercise_sets', values, conditions)
