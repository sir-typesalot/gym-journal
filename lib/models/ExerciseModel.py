from lib.Scribe import Scribe
from lib.models.BaseModel import BaseModel
from lib.DataClasses import Exercise

class ExerciseModel(BaseModel):

    def __init__(self):
        super().__init__()
        self.db = Scribe()

    def create(self, name: str, is_unilateral: bool, is_bodyweight: bool, details: dict):
        # Create dataclass and convert to dict
        exercise = Exercise(name, is_unilateral, is_bodyweight, details).dict()
        try:
            # Derive columns and values from dict
            columns, values = self.split(exercise)
            id = self.db.insert('exercises', columns, values)
            return id
        except:
            # add logging at some point
            print("Unable to create exercise")

    def exists(self, name: str):
        data = self.get({'name': name})
        return True if data else False

    def get(self, search_term: dict):
        exercise = self.db.read('exercises', search_term)
        if not exercise:
            return None
        else:
            exercise = self.sanitize(exercise, Exercise.headers())
            return Exercise(**exercise)
        
    def modify(self, exercise: Exercise):
        conditions = [f"name = '{exercise.name}'"]
        self.db.update('exercises', exercise.dict(), conditions)
        
    def create_new(self, name: str, is_unilateral: bool, is_bodyweight: bool, details: dict):
        exists = self.exists(name)
        if exists:
            raise NameError(f"Exercise {name} already exists")
        else:
            id = self.create(name, is_unilateral, is_bodyweight, details)
            return id
        
    def delete(self, name: str):
        values = {
            'name': name
        }
        conditions = ["name = %(name)s"]
        self.db.drop('exercises', values, conditions)
