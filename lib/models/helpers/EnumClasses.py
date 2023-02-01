from enum import Enum

class Filters(Enum):
    category = 'category'
    difficulty = 'difficulty'
    equipment = 'equipment'
    exerciseName = 'exerciseName'
    family = 'family'
    primaryTargets = 'primaryTargets'
    subFamily = 'subFamily'

    @classmethod
    def has_member_key(cls, key):
        return key in cls.__members__
    
    @classmethod
    def get_member_key(cls, key):
        key = Filters[key].value if cls.has_member_key(key) else None
        if key:
            return key
        else:
            return False

