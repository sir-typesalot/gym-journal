
from lib.models.BaseModel import BaseModel

class ExerciseModel(BaseModel):

    check_value = 'id'

    def __init__(self, exercise_id=None):
        super().__init__()
        self.exercise_info = {}
        if exercise_id:
            self.set_exercise(exercise_id)

    def set_exercise(self, exercise_id):
        self.exercise_id = exercise_id
        self.name = self.get_attribute('name')

    @BaseModel.access_check(check_value)
    def _get_exercise(self):
        if not self.exercise_info:
            result = self._get_('exercises', {'id': self.exercise_id})
            self.exercise_info = result if result else {}
        return self.exercise_info
        
    @BaseModel.access_check(check_value)
    def get_attribute(self, attribute: str):
        return self._get_routine().get(attribute)

    def create_exercise(self, name: str, is_unilateral: bool, is_bodyweight: bool, details: str=None):
        columns = ['name', 'is_unilateral', 'is_bodyweight', 'details']
        values = [name, is_unilateral, is_bodyweight, details]
        try:
            exercise_id = self._insert_('exercises', columns, values)
            return exercise_id
        except:
            print("Trouble creatng exercise")
