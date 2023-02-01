import json
from endpoints.helpers import RequestHelper
from .UserModel import UserModel

class UserLogModel(UserModel):
    
    def __init__(self, user_id=None):
        super(UserModel, self).__init__()
        self.user_id = user_id

    def get_user_logs(self, workout_id=None):
        where = "WHERE user_id = %(user_id)s"
        params = {'user_id': self.user_id}
        if workout_id:
            where += " AND workout_id = %(workout_id)s"
            params['workout_id'] = workout_id
        
        with self.db('dict') as cursor:
            cursor.execute(f"SELECT * from workout_log {where}", params=params)
            result = cursor.fetchall()

        return result

    def create_new_log(self, template):
        
        with self.db() as cursor:
            cursor.execute("""
                INSERT INTO workout_log (user_id,details,date) 
                VALUES (%s, %s, NOW())
            """, (self.user_id, json.dumps(template)))

    def add_load_to_template(self, template, count_list, load_list):

        counter = 0
        template = json.loads(template)

        for exercise in template:
            for work_set in exercise['sets']:

                work_set['count'] = count_list[counter]
                work_set['load'] = load_list[counter]
                counter += 1

        return template
