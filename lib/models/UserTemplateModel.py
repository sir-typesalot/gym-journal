import json
from .UserModel import UserModel

class UserTemplateModel(UserModel):
    
    def __init__(self, user_id=None):
        super(UserModel, self).__init__()
        self.user_id = user_id

    def get_user_template(self, template_id=None):
        
        where = "WHERE user_id = %(user_id)s"
        params = {'user_id': self.user_id}
        if template_id:
            where += " AND t.template_id = %(template_id)s"
            params['template_id'] = template_id
        
        with self.db('dict') as cursor:
            cursor.execute(f"""
                SELECT t.* FROM templates t
                JOIN user_template_map utm ON utm.template_id = t.template_id
                {where}
            """, params=params)
            result = cursor.fetchall()

        return result

    def create_new_template(self, raw_template):

        template = self.process_raw_template(raw_template)
        
        with self.db() as cursor:
            cursor.execute("""
                INSERT INTO templates (name,notes,template,date_created) 
                VALUES (%s, %s, %s, NOW())
            """, (template['title'], template['notes'], json.dumps(template['template'])))
            cursor.execute("SELECT MAX(template_id) AS template_id FROM templates")
            return cursor.fetchone()[0]
    
    def link_user_to_template(self, template_id):
        
        with self.db() as cursor:
            cursor.execute("""
                INSERT INTO user_template_map (template_id,user_id) 
                VALUES (%s, %s)
            """, (template_id, self.user_id))
    
    def process_raw_template(self, raw_template):
        tidy_template = {
            'title': raw_template['title'][0],
            'date': raw_template['date'][0],
            'notes': raw_template['notes'][0],
            'template': []
        }

        raw_template['exercise'].pop(0)
        counter = 1

        for index, exercise in enumerate(raw_template['exercise'], start=1):
            exercise_dict = {
                'name': exercise,
                'sets': []
            }
            sets = int(raw_template['sets'][index])

            for x in range(sets):
                exercise_dict['sets'].append({
                    'unit': raw_template['unit'][counter],
                    'count': raw_template['count'][counter],
                    'pct_1rm': raw_template['pct_1rm'][counter],
                    'rpe': raw_template['rpe'][counter],
                    'rest': raw_template['rest'][counter]
                })

                counter += 1

            tidy_template['template'].append(exercise_dict)
        return tidy_template

    @classmethod
    def convert_json(cls, json_data):
        if isinstance(json_data, str):
            return json.loads(json_data)
        else:
            return json.dumps(json_data)
